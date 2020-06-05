from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


def home(request):
    return render(request, 'blog/home.html')


def animated_me(request):
    return render(request, 'blog/animated-me.html')


class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post