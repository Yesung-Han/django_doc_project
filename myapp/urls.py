from django.urls import path

from myapp.views import *

app_name = 'myapp'

urlpatterns = [

    path('',postListView, name = 'home_view'),
    #path('post/<id>/', @@@@, name = "detail_view"),

    path('add/', PostCreateView.as_view(), name = 'add'),

    path('<int:pk>/update/', PostUpdateView.as_view(), name = 'update'),

    path('<int:pk>/delete/', PostDeleteView.as_view(), name = 'delete'),

    path('logout/', logout, name='logout'),

    path('<int:pk>/', DetailView.as_view(), name = 'detail'),

    path('<int:pk>/comment/',commentCreate, name = 'commentCreate')

]