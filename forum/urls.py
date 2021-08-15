from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostEditView, PostDeleteView, CommentDeleteView, AddDislike, AddLike, AddCommentLike,AddCommentDislike, CommentDeleteView, CommentReplyView

urlpatterns = [
	path('forum', views.forum, name='forum'),
	path('post_list', PostListView.as_view(), name='post-list'),
    path('/post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/edit/<int:pk>/', PostEditView.as_view(), name='post-edit'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_pk>/comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),
    path('post/<int:pk>/like', AddLike.as_view(), name='like'),
    path('post/<int:pk>/dislike', AddDislike.as_view(), name='dislike'),
    path('post/<int:post_pk>/comment/<int:pk>/like', AddCommentLike.as_view(), name='comment-like'),
    path('post/<int:post_pk>/comment/<int:pk>/dislike', AddCommentDislike.as_view(), name='comment-dislike'),
    path('post/<int:post_pk>/comment/reply/<int:pk>', CommentReplyView.as_view(), name='comment-reply'),
    

    



]