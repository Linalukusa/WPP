
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path( 'addreport', views.addreport, name ='addreport'),
    path('reportlist', views.report, name='reportlist'),
    path('myreport', views.userreport, name="myreport")
  

    
] 