from django.urls import path
from .views import PostListView, PostDetailView, NewsSearchView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('search/', NewsSearchView.as_view(), name='news_search'),
]
