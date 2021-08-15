from django.urls import path
from . import views 
from .views import *


urlpatterns = [
    path('discussions', views.discussions, name='discussions'),
    path('new_discussion', views.new_discussion, name='new_discussion'),
    #path('<int:discussion_id>/', views.discussion, name='discussion'),
    #path('<int:discussion_id>/edit/',  views.edit_discussion, name='edit_discussion'),
    path('<int:discussion_id>/comments/new',  views.post_comments, name='new_comment'),
    path('<int:discussion_id>/comments/',  views.get_comments, name='fetch_comments'),
    path('<int:discussion_id>/comments/<int:comment_id>/',  views.delete_comment, name="delete_comments"),
    path('<int:discussion_id>/participants/new/<int:friend_id>/',  views.invite_participant, name="invite_participant"),
    path('<int:discussion_id>/leave',  views.leave_discussion, name="leave_discussion"),
    path( 'mydiscussions', views.userpost, name ='mydiscussions'),

    
]