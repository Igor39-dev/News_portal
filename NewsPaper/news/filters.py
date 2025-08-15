from django_filters import FilterSet, DateFilter
from django import forms
from .models import Post

class PostFilter(FilterSet):
    time_create = DateFilter(
        field_name='time_create',
        lookup_expr='gt',
        widget=forms.DateInput(attrs={'type': 'date'})
    )


    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'author__user__username': ['icontains'],
        }