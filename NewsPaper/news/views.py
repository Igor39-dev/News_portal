from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Category, Post
from datetime import datetime
from .filters import PostFilter
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.core.cache import cache

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

    def get_object(self, queryset=None):
        post_id = self.kwargs['pk']
        cache_key = f'post_{post_id}'
        obj = cache.get(cache_key)
        if not obj:
            obj = super().get_object(queryset=queryset)
            cache.set(cache_key, obj)
        return obj

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
    
class NewsCreateView(PermissionRequiredMixin, CreateView):
    # добавление ограничения
    permission_required = ('news.add_post')
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = Post.NEWS
        return super().form_valid(form)
    
class NewsUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    # добавление ограничения
    permission_required = ('news.change_post')
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

class ArticleCreateView(PermissionRequiredMixin, CreateView):
    # добавление ограничения
    permission_required = ('news.add_post')
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = Post.ARTICLE
        return super().form_valid(form)
    
class ArticleUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    # добавление ограничения
    permission_required = ('news.change_post')
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

class ArticleDeleteView(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('post_list')


@login_required
def subscribe_to_category(request, pk):
    category = get_object_or_404(Category, id=pk)
    user = request.user
    if user in category.subscribers.all():
        category.subscribers.remove(user)
    else:
        category.subscribers.add(user)

    return redirect(request.META.get('HTTP_REFERER', '/'))


def test_send_email(request):
    send_mail(
        subject='Тестовое письмо',
        message='Привет! Это тест.',
        from_email='gorokhov-igor.g@yandex.ru',
        recipient_list=['19gorokhov90@gmail.com'],
    )
    return HttpResponse("Письмо отправлено!")
