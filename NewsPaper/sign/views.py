from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'

@login_required
def become_author(request):
    authors_group, created = Group.objects.get_or_create(name='authors')
    request.user.groups.add(authors_group)
    return redirect('/')
