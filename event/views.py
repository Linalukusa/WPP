from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, Http404, HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect
#from authentication.models import Profile
from .forms import *
from .models import *

from django.http import HttpResponse, Http404
from django.core.paginator import (Paginator, EmptyPage, PageNotAnInteger)




@login_required
def list_events(request):
    all_research = Event.objects.all()
    paginator = Paginator(all_research, 6) # 2 posts in each page
    page = request.GET.get('page')
    try:
       posts = paginator.page(page)
    except PageNotAnInteger:
       # If page is not an integer deliver the first page
       posts = paginator.page(1)
    except EmptyPage:
       # If page is out of range deliver last page of results
       posts = paginator.page(paginator.num_pages)

    context = { 'posts':posts }
    return render(request, 'event/event_list.html',context)



@login_required
def userpost(request):
    user_posts = Event.objects.filter(owner=request.user).order_by('-created_time')
    paginator = Paginator(user_posts, 6) # 2 posts in each page
    page = request.GET.get('page')
    try:
       posts = paginator.page(page)
    except PageNotAnInteger:
       # If page is not an integer deliver the first page
       posts = paginator.page(1)
    except EmptyPage:
       # If page is out of range deliver last page of results
       posts = paginator.page(paginator.num_pages)
    context={'posts':posts}
    return render(request,  'event/myevents.html', context=context)


@login_required
def event_details(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
        participants = EventParticipant.objects.filter(event=event)

        # We are trying to see if user is invited to this event
        find_user_participation = EventParticipant.objects.filter(event=event, invitee=request.user)
        is_participating = len(find_user_participation) > 0

        # Finding out if current user is the one created this event
        is_owner = event.owner == request.user
        context = {
            'event': event,
            'participants': participants,
            'is_participating': is_participating,
            'accepted': is_participating and find_user_participation[0].accepted,
            'is_owner': is_owner
        }
        return render(request, 'event/event_details.html', context)
    except Event.DoesNotExist:
        raise Http404('Event does not exist')


@login_required
def event_new(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            added_event = Event(
                owner=request.user,
                name=cleaned_data.get('name'),
                description=cleaned_data.get('description'),
                location=cleaned_data.get('location'),
                start_time=cleaned_data.get('start_time'),
                end_time=cleaned_data.get('end_time'),
                logo=cleaned_data.get('logo'),
                website=cleaned_data.get('website'),
                email=cleaned_data.get('email'),
            )
            added_event.save()
            messages.success(request, 'Event has been created')
            return redirect('dashboard')
    else:
        form = EventForm()

    context = {
        'form': form,
}

    return render(request, 'event/addevent.html', context)






@login_required
@require_http_methods(['POST'])
def invite_participant(request, event_id, friend_id):
    """
    This view handles request to add a friend to an event
    :param event_id: id of the event
    :param friend_id: user id of the friend
    """
    event = Event.objects.get(id=event_id)
    inviter = request.user
    friend = Profile.objects.get(id=friend_id)

    # Find out if this friend is already invited
    find_participation_friend_invitee = EventParticipant.objects.filter(event=event, invitee=friend)

    # Find out if the inviter is already participating the event or the event owner
    find_participation_inviter = EventParticipant.objects.filter(event=event, invitee=inviter, accepted=True)
    if len(find_participation_inviter) == 0 and event.owner != inviter:
        return HttpResponseForbidden('You are not a participant of this')

    if len(find_participation_friend_invitee) == 0:
        new_participant = EventParticipant(event=event, inviter=inviter, invitee=friend)
        new_participant.save()
        messages.success(request, 'Invited friend')
        return redirect(event.get_absolute_url())
    return HttpResponseBadRequest('Friend is already invited')


@login_required
@require_http_methods(['POST'])
def accept_participation(request, event_id):
    """
    As the user if they want to accept an invitation to an event they will request to this
    view
    """
    try:
        event = Event.objects.get(id=event_id)
        invitee = EventParticipant.objects.get(event=event, invitee=request.user)
        if invitee.accepted:
            return HttpResponseBadRequest('You already accepted')
        messages.success(request, 'Yay! You are now officially in this event!')
        invitee.accepted = True
        invitee.save()
        return redirect(event.get_absolute_url())
    except Event.DoesNotExist:
        raise Http404('Event not found')
    except EventParticipant.DoesNotExist:
        raise Http404('You are not invited')


@login_required
@require_http_methods(['POST'])
def leave_or_reject_event(request, event_id):
    """
    If user want to reject or leave an event, they will request this view. Since a participation
    is saved as a Model so deleting that both means leaving or rejecting
    :return:
    """
    try:
        event = Event.objects.get(id=event_id)
        invitee = EventParticipant.objects.get(event=event, invitee=request.user)
        invitee.delete()
        messages.success(request, 'You have been out of this event!')
        return redirect(event.get_absolute_url())
    except Event.DoesNotExist:
        raise Http404('Event not found')
    except EventParticipant.DoesNotExist:
        raise Http404('You are not invited')


@login_required
def event_edit(request, event_id):
    """
    This view render UI to edit an event
    """
    event_to_update = Event.objects.get(id=event_id)
    if request.user != event_to_update.owner:
        return HttpResponseForbidden('You are not the owner of this event!')
    if request.method == 'POST':
        form = EventCreateAndUpdateForm(request.POST, instance=event_to_update)
        if form.is_valid():
            edited_event = form.save()
            messages.success(request, 'Event has been updated')
            return redirect(edited_event.get_absolute_url())
        else:
            return render(request, 'event/event_edit.html', {'form': form})
    form = EventCreateAndUpdateForm(instance=event_to_update)
    return render(request, 'event/event_edit.html', {'form': form})


@login_required
def delete_event(request, event_id):
    """
    The owner of an event can delete the event by requesting this link
    """
    try:
        event = Event.objects.get(id=event_id)

        # All participation needs to be deleted as well
        participants = EventParticipant.objects.filter(event=event)
        for participant in participants:
            participant.delete()

        if event.owner != request.user:
            return HttpResponseForbidden('You are not the owner of this event')
        event.delete()
        return redirect('events')
    except Event.DoesNotExist:
        raise Http404('Event does not exist')