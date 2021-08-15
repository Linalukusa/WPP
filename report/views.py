from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse, Http404, HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from .forms import ReportCreationForm, ReportUpdateForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
#from authentication.models import Profile
from agravatar.tags import gravatar_url
from django.http import HttpResponse, Http404
from django.core.paginator import (Paginator, EmptyPage, PageNotAnInteger)



from .models import *


@login_required
def report(request):
    '''A view where all discussions are shown'''
    all_resources = Report.objects.all()
    paginator = Paginator(all_resources, 4) # 2 posts in each page
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
    return render(request, 'report/reportlist.html', context=context)

@login_required
def userreport(request):
    user_posts = Report.objects.filter(owner=request.user).order_by('-created_time')
    paginator = Paginator(user_posts, 4) # 2 posts in each page
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
    return render(request,  'report/myreport.html', context=context)


def addreport (request):
    return render(request, 'report/addreport.html')