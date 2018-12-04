from django.urls import path

from myapp.views import *

app_name = 'myapp'

urlpatterns = [

    path('',PostLV.as_view(), name = 'home_view'),
    #path('post/<id>/', @@@@, name = "detail_view"),

]