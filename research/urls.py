
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path( 'addresearch', views.new_research, name ='addresearch'),
    path( 'research_list', views.researchs, name ='research_list'),
    path('myresearch', views.userpost, name="myresearch"),
    path('<int:research_id>/', views.research, name="research"),
    path('<int:research_id>/edit/',  views.edit_research, name='edit_research'),
    path('research/', ResearchSearch.as_view(), name='research-search'),





  

    
] 