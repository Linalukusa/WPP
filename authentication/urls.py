
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *
from .views import SignUpView, ActivateAccount
from .views import ProfileView


urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'), 
    path('signin', views.signin, name='signin'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
	path('dashboard', dashboard.as_view(), name='dashboard'),
    path('logout', views.logout_user, name='logout'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('search/', UserSearch.as_view(), name='profile-search'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile-edit'),
    path( 'browsepractitioners', views.browsepractitioners, name ='browsepractitioners'),



  

    
] 