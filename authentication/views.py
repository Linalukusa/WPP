from django.shortcuts import render,redirect,get_object_or_404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, UpdateView
from .forms import SignUpForm
from django.contrib.auth.models import User

from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import login as dj_login
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.utils.encoding import force_text
from django.http import HttpResponse
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Profile
from forum.models import Post
from django.db.models import Q
from django.core.paginator import (Paginator, EmptyPage, PageNotAnInteger)
from forum.models import Post, Comment
from forum.forms import PostForm, CommentForm
from event.models import Event

# Create your views here.


# Create your views here.


# Sign Up View
class SignUpView(View):
    form_class = SignUpForm
    template_name = 'authentication/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():

            user = form.save(commit=False)
            user.is_active = False # Deactivate account till it is confirmed
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate Your Water People & Place Account'
            message = render_to_string('authentication/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)

            return HttpResponse('We have sent you an email, please confirm your email address to complete registration')
        return render(request, self.template_name, {'form': form})

def forgot_password (request):
    return render(request, 'authentication/forgot_password.html')



class dashboard(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        all_event = Event.objects.all()
        form = PostForm()

        context = {
            'post_list': posts,
            'form': form,
            'event':all_event,
        }
        return render(request, 'authentication/dashboard.html', context)

    def post(self, request, *args, **kwargs):
        posts = Post.objects.all()
        form = PostForm(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

        context = {
            'post_list': posts,
            'form': form,
        }
        return render(request, 'authentication/dashboard.html', context)

@login_required
def logout_user(request):
	logout(request)
	messages.info(request,('You are now logged out'))
	return redirect('/')


def signin (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(username=username, password=password)
        if user is not None:
            dj_login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        messages.error(request, "Invalid username or password.")
    form = SignUpForm() 
    return render(request, 'authentication/signin.html', {'form': form})


class ActivateAccount(View):

    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.profile.email_confirmed = True
            user.save()
            login (request, user)
            messages.success(request, ('Your account have been confirmed.'))
            return redirect('signin')
        else:
            messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
            return redirect('signin')


class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        user = profile.user
        posts = Post.objects.filter(author=user).order_by('-created_on')

        context = {
            'user': user,
            'profile': profile,
            'posts': posts,
        }
        return render(request, 'authentication/profile.html', context)

def browsepractitioners (request):
    profile = Profile.objects.all()
    paginator = Paginator(profile, 6) # 2 posts in each page
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
    return render(request, 'practitionner/browsepractitionners.html', context)

class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        user = profile.user
        posts = Post.objects.filter(author=user).order_by('-created_on')

        context = {
            'user': user,
            'profile': profile,
            'posts': posts,
        }
        return render(request, 'partials/_sidebar.html', context)

class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    fields = ['name', 'bio', 'birth_date', 'location', 'picture']
    template_name = 'authentication/profile_edit.html'
    
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': pk})
    
    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user


class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    fields = ['name', 'bio', 'picture']
    template_name = 'authentication/profile_edit.html'
    
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': pk})
    
    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user


class UserSearch(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        profile_list = Profile.objects.filter(
            Q(user__username__icontains=query)
        )

        context = {
            'profile_list': profile_list
        }

        return render(request, 'authentication/search.html', context)