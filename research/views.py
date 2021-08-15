from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse, Http404, HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from .forms import ResearchCreationForm, ResearchUpdateForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from authentication.models import Profile
from agravatar.tags import gravatar_url
from django.http import HttpResponse, Http404
from django.core.paginator import (Paginator, EmptyPage, PageNotAnInteger)
from django.db.models import Q
from django.views.generic import View, UpdateView
from .models import *



@login_required
def researchs(request):
    '''A view where all discussions are shown'''
    all_research = Research.objects.all()
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
    return render(request, 'research/research_list.html', context=context)

@login_required
def userpost(request):
    user_posts = Research.objects.filter(owner=request.user).order_by('-created_time')
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
    return render(request,  'research/myresearch.html', context=context)


@login_required
def new_research(request):
    '''A view where new discussion can be created'''
    if request.method == 'POST':
        form = ResearchCreationForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            added_research = Research(
                title = cleaned_data.get('title'),
                leadresearcher = cleaned_data.get('leadresearcher'),
                publisher = cleaned_data.get('publisher'),
                city = cleaned_data.get('city'),
                researchfile = cleaned_data.get('researchfile'),
                startdate =cleaned_data.get('startdate'),
                enddate = cleaned_data.get('enddate'),
                description = cleaned_data.get('description'),
                collab = cleaned_data.get('collab'),
                funding = cleaned_data.get('funding'),
                website= cleaned_data.get('website'),
                email= cleaned_data.get('email'),
                owner=request.user
            )
            added_research.save()
            messages.success(request, 'Project has been created')
            return redirect('dashboard')
    else:
        form = ResearchCreationForm()

    context = {
        'form': form,
}

    return render(request, 'research/addresearch.html', context)


 

@login_required
def research(request, research_id):
    '''A view  where a discussion, with the ID of discussion_id, can be viewed'''
    current_research = Research.objects.get(id=research_id)
    participants = ResearchParticipant.objects.filter(research=current_research)
    find_user_participate = ResearchParticipant.objects.filter(
        research=current_research, 
        participant=request.user
    )  
    is_owner = request.user == current_research.owner
    is_participating = len(find_user_participate) > 0
    context = {
        'research': current_research,
        'participants': participants,
        'is_participating': is_participating,
        'is_owner': is_owner
    }

    return render(request, 'research/research_details.html', context)

@login_required
def edit_research(request, research_id):
    '''A view where a discussion, with the ID of discussion_id, can be edited'''
    research_to_update = Research.objects.get(id__exact=research_id)
    if request.method == 'POST':
        form = ResearchUpdateForm(request.POST, instance=research_to_update)
        if form.is_valid():
            edited_research = form.save()
            messages.success(request, 'Research has been updated')
            return redirect(edited_research.get_absolute_url())
    else:
        form = ResearchUpdateForm(instance=research_to_update)

    context = {
        'form': form,
    }

    return render(request, 'research/research_edit.html', context)


@login_required
def edit_research(request, research_id):
    '''A view where a discussion, with the ID of discussion_id, can be edited'''
    research_to_update = Research.objects.get(id__exact=research_id)
    if request.method == 'POST':
        form = ResearchUpdateForm(request.POST, instance=research_to_update)
        if form.is_valid():
            edited_research = form.save()
            messages.success(request, 'research has been updated')
            return redirect('myresearch')
    else:
        form = ResearchUpdateForm(instance=research_to_update)

    context = {
        'form': form,
    }

    return render(request, 'research/research_edit.html', context)


class ResearchSearch(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        research_list = Research.objects.filter(Q(title__icontains=query) | Q(publisher__icontains=query) |Q(city__icontains=query) )

        context = {
            'research_list': research_list
        }

        return render(request, 'research/search.html', context)

