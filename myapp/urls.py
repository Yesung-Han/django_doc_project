from django.urls import path

from myapp.views import *

app_name = 'myapp'

urlpatterns = [

    path('logout/', logout, name='logout'),


    path('',postListView, name = 'home_view'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),

    path('add/', PostCreateView.as_view(), name = 'add'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name = 'update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name = 'delete'),

    path('<int:postId>/UComment_<int:pk>',CommentUpdateView.as_view(), name = 'comment_update'),
    path('<int:postId>/DComment_<int:pk>',CommentDeleteView.as_view(), name = 'comment_delete'),

    path('<int:postId>/CRepost/',RePostCreate.as_view(), name = 'add_repost'),
    path('<int:PcommentId>/addRecomment/',ReCommentCreateView.as_view(), name = 'add_recomment'),
]

