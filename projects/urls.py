
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *


urlpatterns = [
    path( 'addproject', views.new_project, name ='addproject'),
    path( 'project_list', views.projects, name ='project_list'),
    #path('<int:project_id>/', views.project, name='project'),
    #path('<int:project_id>/edit/',  views.edit_project, name='project_edit'),
    path( 'myproject', views.userpost, name ='myproject'),
    path( 'projects', views.projecthomepage, name ='projects'),

   
] 
