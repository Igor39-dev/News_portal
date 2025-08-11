from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime
# Create your views here.

class PostListView(ListView):
    model = Post
    ordering = ['-time_create']
    template_name = 'posts.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_create'] = datetime.utcnow()
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

