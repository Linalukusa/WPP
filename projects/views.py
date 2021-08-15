from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse, Http404, HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from .forms import ProjectCreationForm, ProjectUpdateForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from authentication.models import Profile
from agravatar.tags import gravatar_url
from django.http import HttpResponse, Http404
from django.core.paginator import (Paginator, EmptyPage, PageNotAnInteger)



from .models import *


@login_required
def projects(request):
    '''A view where all discussions are shown'''
    projects = Project.objects.all()
    paginator = Paginator(projects, 6) # 2 posts in each page
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
    return render(request, 'projects/project_list.html', context=context)

def projecthomepage(request):
    '''A view where all discussions are shown'''
    projects = Project.objects.all()
    paginator = Paginator(projects, 6) # 2 posts in each page
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
    return render(request, 'homepage/projects.html', context=context)


@login_required
def userpost(request):
    user_posts = Project.objects.filter(owner=request.user).order_by('-created_time')
    paginator = Paginator(user_posts,6) # 2 posts in each page
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
    return render(request,  'projects/myproject.html', context=context)


@login_required
def new_project(request):
    '''A view where new discussion can be created'''
    if request.method == 'POST':
        form = ProjectCreationForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            added_project = Project(
                leadorganisations = cleaned_data.get('leadorganisations'),
                projectname = cleaned_data.get('projectname'),
                publisher = cleaned_data.get('publisher'),
                city = cleaned_data.get('city'),
                projectlogo = cleaned_data.get('projectlogo'),
                maintheme = cleaned_data.get('maintheme'),
                topic = cleaned_data.get('topic'),
                website = cleaned_data.get('website'),
                email = cleaned_data.get('email'),
                startdate =cleaned_data.get('startdate'),
                enddate = cleaned_data.get('enddate'),
                projectsummary = cleaned_data.get('projectsummary'),
                whatwedo = cleaned_data.get('whatwedo'),
                howwedo = cleaned_data.get('howwedo'),
                achieved = cleaned_data.get('achieved'),
                owner=request.user
            )
            added_project.save()
            messages.success(request, 'Project has been created')
            return redirect('dashboard')
    else:
        form = ProjectCreationForm()

    context = {
        'form': form,
}

    return render(request, 'projects/addproject.html', context)


@login_required
def edit_project(request, project_id):
    '''A view where a discussion, with the ID of discussion_id, can be edited'''
    project_to_update = Project.objects.get(id__exact=project_id)
    if request.method == 'POST':
        form = ProjectUpdateForm(request.POST, instance=project_to_update)
        if form.is_valid():
            edited_project = form.save()
            messages.success(request, 'Project has been updated')
            return redirect(edited_project.get_absolute_url())
    else:
        form = ProjectUpdateForm(instance=project_to_update)

    context = {
        'form': form,
    }

    return render(request, 'projects/project_edit.html', context)


@login_required
def project(request, project_id):
    '''A view  where a discussion, with the ID of discussion_id, can be viewed'''
    current_project = Project.objects.get(id=project_id)
    participants =ProjectParticipant.objects.filter(project=current_project)
    find_user_project = ProjectParticipant.objects.filter(
        project=current_project, 
        participant=request.user
    )
    is_owner = request.user == current_project.owner
    context = {
        'project': current_project,
        'participants': participants,
        'is_owner': is_owner
    }

    return render(request, 'projects/project_details.html', context)

