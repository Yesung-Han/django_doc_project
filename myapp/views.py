from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from myapp.models import Post

class PostLV(ListView):

    model = Post

    template_name = 'myapp/home.html'
    context_object_name = 'posts'

    paginate_by = 2
