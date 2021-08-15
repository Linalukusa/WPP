from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse, Http404, HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from .forms import OrganisationCreationForm, OrganisationUpdateForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from authentication.models import Profile
from agravatar.tags import gravatar_url
from django.http import HttpResponse, Http404
from django.core.paginator import (Paginator, EmptyPage, PageNotAnInteger)



from .models import *
import requests
from bs4 import BeautifulSoup
# Create your views here.


@login_required
def addorganisation(request):
    '''A view where new discussion can be created'''
    if request.method == 'POST':
        form = OrganisationCreationForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            added_organisation = Organisation(
                organisationname = cleaned_data.get('organisationname'),
                city = cleaned_data.get('city'),
                projectlogo = cleaned_data.get('projectlogo'),
                vision = cleaned_data.get('vision'),
                mission =cleaned_data.get('mission'),
                website = cleaned_data.get('website'),
                achieved = cleaned_data.get('achieved'),
                owner=request.user
            )
            added_organisation.save()
            messages.success(request, 'Organisation has been created')
            return redirect('organisations')
    else:
        form = OrganisationCreationForm()

    context = {
        'form': form,
}

    return render(request, 'organisation/addorganisation.html', context)


@login_required
def organisations(request):
    user_posts = Organisation.objects.all()
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
    return render(request,  'organisation/organisations.html', context=context)

@login_required
def userpost(request):
    user_posts = Organisation.objects.filter(owner=request.user).order_by('-created_time')
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
    return render(request,  'organisation/myorganisation.html', context=context)



@login_required
def organisation(request, organisation_id):
    '''A view  where an organisation, with the ID oforganisation_id, can be viewed'''
    current_organisation = Organisation.objects.get(id=organisation_id)
    participants = OrganisationParticipant.objects.filter(organisation=current_organisation)
    find_user_participate = OrganisationParticipant.objects.filter(
        organisation=current_organisation, 
        participant=request.user
    )  
    is_owner = request.user == current_organisation.owner
    is_participating = len(find_user_participate) > 0
    context = {
        'organisation': current_organisation,
        'participants': participants,
        'is_participating': is_participating,
        'is_owner': is_owner
    }

    return render(request, 'organisation/organisation_details.html', context)