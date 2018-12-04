from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin, ModelFormMixin

from myapp.models import Post, Comment
from django.contrib.auth import logout as django_logout
from django.shortcuts import redirect

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from newSite.views import LoginRequiredMixin
from .forms import CommentForm

def logout(request):
    django_logout(request)
    return redirect('myapp:home_view')

def postListView(request):
    post_list = Post.objects.all()
    #search
    q = request.GET.get('q','')
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

def commentCreate(request, pk):

    post = get_object_or_404(Post, pk = pk)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.linkedPost = post
            comment.writer = request.user
            comment.save()
            return redirect('myapp:detail', pk = post.pk)
    else:
        form = CommentForm()
    return render(request, 'myapp/add_comment_to_post.html',{'form':form})

class DetailView(FormMixin, DetailView):
    model = Post
    template_name = 'myapp/detail.html'
    form_class = CommentForm

    def get_initial(self):
        return {"linkedPost" : self.get_object(),
                "writer" : self.request.user}

    def get_success_url(self):
        return reverse('myapp:detail', self.object.id)

    def get_context_data(self, **kwargs):
        context = super(DetailView,self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(linkedPost=kwargs['object'])
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            print("11111111")
            return self.form_valid(form)
        else:
            print("2222222")
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.linkedPost = self
        comment.writer = self.request.user
        comment.save()
        return super().form_valid(form)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title_text','content']
    success_url = reverse_lazy('myapp:home_view')

    def form_valid(self, form):
        form.instance.writer = self.request.user
        return super(PostCreateView,self).form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title_text', 'content']
    success_url = reverse_lazy('myapp:home_view')


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('myapp:home_view')
