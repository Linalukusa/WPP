from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse, Http404, HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from .forms import DiscussionCreationForm, DiscussionUpdateForm, DiscussionCommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from authentication.models import Profile
from agravatar.tags import gravatar_url
from django.http import HttpResponse, Http404
from .models import *


@login_required
def discussions(request):
    '''A view where all discussions are shown'''
    all_discussions = Discussion.objects.all()
    context = {
        'discussions': all_discussions
    }
    return render(request, 'discussion/discussion_list.html', context=context)

@login_required
def userpost(request):
    user_posts = Discussion.objects.filter(owner=request.user).order_by('-created_time')
    return render(request,  'discussion/mydiscussions.html', {'posts': user_posts})

@login_required
def new_discussion(request):
    '''A view where new discussion can be created'''
    if request.method == 'POST':
        form = DiscussionCreationForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            added_discussion = Discussion(
                title=cleaned_data.get('title'),
                description=cleaned_data.get('description'),
                owner=request.user
            )
            added_discussion.save()
            self_participation = ParticipantDiscussion(
                participant=request.user,
                discussion=added_discussion
            )
            self_participation.save()
            messages.success(request, 'Discussion has been created')
            return redirect('mydiscussions')
    else:
        form = DiscussionCreationForm()

    context = {
        'form': form,
}

    return render(request, 'discussion/discussion_new.html', context)






@login_required
@require_http_methods(["POST"])
def invite_participant(request, discussion_id, friend_id):
    '''
        The function is called when the user adds a friend, with the ID of
        friend_id, to a discussion, with the ID of discussion_id. If both exist
        and the friend is not a participant of the discussion already, they are
        added as a participant.
    '''
    try:
        friend = Profile.objects.get(id=friend_id)
        discussion = Discussion.objects.get(id=discussion_id)
        find_participant = ParticipantDiscussion.objects.filter(
            participant=friend,
            discussion=discussion
        )
        if len(find_participant) > 0:
            return HttpResponseBadRequest('Friend is already in the discussion')
        new_participant = ParticipantDiscussion(
            participant=friend,
            discussion=discussion
        )
        new_participant.save()
        return redirect(discussion.get_absolute_url())
    except Profile.DoesNotExist:
        raise Http404('Friend not found')
    except Discussion.DoesNotExist:
        raise Http404('Discussion not found')
    return HttpResponse('OK')


@login_required
def leave_discussion(request, discussion_id):
    '''
        The function is called when the user leaves a discussion, with the ID
        of discussion_id. The user is removed from the discussion.
    '''
    try:
        discussion = Discussion.objects.get(id=discussion_id)
        participants = ParticipantDiscussion.objects.filter(participant=request.user,discussion=discussion)
        if (len(participants) == 0):
            raise Http404('Participant is not in this discussion!')

        # There should be only one participant (the user) at this stage, but if
        # the user has ended up multiple times on the participants for any
        # reason it gets fixed here.
        for participant in participants:
            participant.delete()

        return redirect('/discussions')
    except ParticipantDiscussion.DoesNotExist:
        raise Http404('Participant not found')
    return HttpResponse('OK')


@login_required
@require_http_methods(["GET"])
def get_comments(request, discussion_id):
    '''
        The function gathers all comments in a discussion, with the ID of
        discussion_id, and returns them as a JSON response.
    '''
    try:
        current_discussion = Discussion.objects.get(id=discussion_id)
        comments = DiscussionComment.objects.filter(discussion=current_discussion)
        response = []
        for comment in comments:
            response.append({
                'id': comment.id,
                'content': comment.content,
                'created_time': comment.created_time.isoformat(),
                'commenter': {
                    'name': comment.commenter.name(),
                    'profile_picture': gravatar_url(comment.commenter.email, 20)
                },
                'can_delete': comment.commenter == request.user or
                              request.user == current_discussion.owner
            })
        return JsonResponse({'comments': response})
    except Discussion.DoesNotExist:
        raise Http404('Discussion not found')


@login_required
@require_http_methods(["POST"])
def post_comments(request, discussion_id):
    '''
        The function is called when the user comments on a discussion, with the
        ID of discussion_id. The comment is added to the discussion if the user
        is a participant of it and the comment is valid.
    '''
    try:
        current_discussion = Discussion.objects.get(id=discussion_id)
        participants = ParticipantDiscussion.objects.filter(
            discussion=current_discussion,
            participant=request.user
        )
        if len(participants) == 0:
            return HttpResponseForbidden('You cannot comment to this discussion!')
        form = DiscussionCommentForm(request.POST)
        if form.is_valid():
            new_comment = DiscussionComment(
                content=form.cleaned_data.get('content'),
                commenter=request.user,
                discussion=current_discussion
            )
            new_comment.save()
            return HttpResponse('OK')
        return HttpResponseBadRequest('Not a valid comment')
    except Discussion.DoesNotExist: 
        raise Http404('Discussion not found')


@login_required()
@require_http_methods(["DELETE"])
def delete_comment(request, discussion_id, comment_id):
    '''
        The function is called when the user removes a comment, with the ID of
        comment_id, from a discussion, with the ID of discussion_id. The
        comment is removed if the user is authenticated to do so.
    '''
    try:
        current_discussion = Discussion.objects.get(id=discussion_id)
        current_comment = DiscussionComment.objects.get(id=comment_id)
        commenter = current_comment.commenter
        discussion_owner = current_discussion.owner
        if request.user == commenter or request.user == discussion_owner:
            current_comment.delete()
            return HttpResponse('OK')
        return HttpResponseForbidden('You cannot delete this comment')
    except Discussion.DoesNotExist:
        raise Http404('Discussion not found')
    except DiscussionComment.DoesNotExist:
        raise Http404('Comment not found')