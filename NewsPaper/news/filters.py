from django_filters import FilterSet, DateFilter, CharFilter
from django import forms
from .models import Post

class PostFilter(FilterSet):
    time_create = DateFilter(
        field_name='time_create',
        lookup_expr='gt',
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='по дате после'
    )

    title = CharFilter(
        field_name='title',
        lookup_expr='iregex',
        label='поиск по тексту'
    )

    author__user__username = CharFilter(
        field_name='author__user__username',
        lookup_expr='iregex',
        label='автор',
    )

    class Meta:
        model = Post
        fields = []