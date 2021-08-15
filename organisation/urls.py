from django.urls import path
from . import views

from .views import *
urlpatterns = [
  
    path('addorganisation', views.addorganisation, name="addorganisation"),
    path('organisations', views.organisations, name="organisations"),
    path('myorganisation', views.userpost, name="myorganisation"),
    path('<int:organisation_id>/', views.organisation, name="organisation"),




]