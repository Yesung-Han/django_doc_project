import null
from django.db.models import *
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin, ModelFormMixin

from myapp.models import Post, Comment
from django.contrib.auth import logout as django_logout
from django.shortcuts import redirect

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from newSite.views import LoginRequiredMixin
from .forms import CommentForm
import logging

def logout(request):
    django_logout(request)
    return redirect('myapp:home_view')

def updateOrder(self):
    update_posts = Post.objects.filter(g_order=self.object.g_order)
    recentOrder = Post.objects.all().order_by('-g_order')[0].g_order

    for post in update_posts:
        post.g_order = recentOrder + 1
        post.save()

    post = self.object
    post.g_order = recentOrder + 1
    post.save()

def postListView(request):
    post_list = Post.objects.all()
    if post_list != null:
        recentOrder = Post.objects.all().order_by('-g_order')[0].g_order
        for post in post_list:
            if post.g_order == 0:
                post.g_order = recentOrder+1
                post.save()

    post_list = Post.objects.all().order_by('-g_order','create_date')

    #search

    q = request.GET.get('qf','')
    if q:
        post_list = post_list.filter(title_text__icontains=q)


    page = request.GET.get('page',1)

    paginator = Paginator(post_list, 5)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'myapp/home.html', {'posts': posts})

class DetailView(FormMixin, DetailView):
    model = Post
    template_name = 'myapp/detail.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('myapp:detail', kwargs={'pk' : self.object.id})

    def get_context_data(self, **kwargs):
        context = super(DetailView,self).get_context_data(**kwargs)

        comments = Comment.objects.filter(linkedPost=kwargs['object']).order_by('modify_date')
        for comment in comments:
            if comment.depth == 0 & comment.parent_comment != comment.id:
                comment.parent_comment = comment.id
                comment.save()

        comments = comments.order_by('parent_comment','create_date',)

        context['comments'] = comments
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.linkedPost = self.get_object()
        comment.writer = self.request.user
        comment.modify_date = timezone.now()
        form.save()
        return super(DetailView,self).form_valid(form)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title_text','content']
    success_url = reverse_lazy('myapp:home_view')

    def form_valid(self, form):
        form.instance.writer = self.request.user
        form.instance.modify_date = timezone.now()
        return super(PostCreateView,self).form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title_text', 'content']
    success_url = reverse_lazy('myapp:home_view')

    def form_valid(self, form):
        #
        updateOrder(self)
        #
        form.instance.modify_date = timezone.now()
        return super(PostUpdateView, self).form_valid(form)

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('myapp:home_view')

##
class RePostCreate(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title_text', 'content']
    template_name = 'myapp/repost_form.html'
    success_url = reverse_lazy('myapp:home_view')

    def get_parentPost(self):
        parentPost = Post.objects.get(id=self.kwargs['postId'])
        return  parentPost

    def get_context_data(self, **kwargs):
        context = super(RePostCreate,self).get_context_data(**kwargs)
        context['pp'] = self.get_parentPost()
        return context

    def form_valid(self, form):
        parentPost = self.get_parentPost()
        recentOrder = Post.objects.all().order_by('-g_order')[0].g_order

        update_posts = Post.objects.filter(g_order=parentPost.g_order)
        for post in update_posts:
            post.g_order = recentOrder + 1
            post.save()

        parentPost.g_order = recentOrder + 1
        parentPost.save()
        form.instance.initRePost(parentPost)

        form.instance.writer = self.request.user
        form.instance.modify_date = timezone.now()
        return super(RePostCreate, self).form_valid(form)

##
class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ['content',]

    def get_success_url(self):
        return reverse('myapp:detail', kwargs={'pk': self.object.linkedPost.id})

    def form_valid(self, form):
        form.instance.modify_date = timezone.now()
        return super(CommentUpdateView, self).form_valid(form)

class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    def get_success_url(self):
        return reverse('myapp:detail', kwargs={'pk': self.object.linkedPost.id})

##
class ReCommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']
    template_name = 'myapp/recomment_add.html'

    def get_success_url(self):
        return reverse('myapp:detail', kwargs={'pk': self.object.linkedPost.id})

    def get_context_data(self, **kwargs):
        context = super(ReCommentCreateView,self).get_context_data(**kwargs)
        context['pc'] = Comment.objects.get(id = self.kwargs['PcommentId'])
        return context

    def form_valid(self, form):
        parentComment = self.get_context_data()['pc']
        form.instance.initReComment(parentComment)
        form.instance.linkedPost = parentComment.linkedPost
        form.instance.writer = self.request.user
        form.instance.modify_date = timezone.now()
        return super(ReCommentCreateView, self).form_valid(form)