from django.urls import path
from .views import PostListView, PostDetailView, NewsSearchView, NewsCreateView, NewsUpdateView, NewsDeleteView, ArticleCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('search/', NewsSearchView.as_view(), name='news_search'),
    path('create/', NewsCreateView.as_view(), name='news_create'),
    path('<int:pk>/edit/', NewsUpdateView.as_view(), name='news_edit'),
    path('<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]
