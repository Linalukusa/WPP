from django.urls import path
from . import views
from .views import *
urlpatterns = [
    path('event_list', views.list_events, name='event_list'),
    path('addevent', views.event_new, name='addevent'),
    path('myevents', views.userpost, name="myevents"),

    
]