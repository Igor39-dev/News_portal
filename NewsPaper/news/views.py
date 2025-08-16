from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from datetime import datetime
from .filters import PostFilter
from .forms import PostForm

# Create your views here.
class PostListView(ListView):
    model = Post
    ordering = ['-time_create']
    template_name = 'posts.html'
    context_object_name = 'posts'
    # ограничение в 10 новостей
    paginate_by = 10


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_create'] = datetime.utcnow()
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

# страница для поиска новостей /news/search
class NewsSearchView(ListView):
    model = Post
    template_name = 'news_search.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context
    
class NewsCreateView(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = Post.NEWS
        return super().form_valid(form)
    
class NewsUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'news_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = Post.NEWS
        return super().form_valid(form)
    
class NewsDeleteView(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('post_list')

class ArticleCreateView(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = Post.ARTICLE
        return super().form_valid(form)
    
class ArticleUpdateView(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

class ArticleDeleteView(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('post_list')