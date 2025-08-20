from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group

class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        common_group, created = Group.objects.get_or_create(name='common')
        user.groups.add(common_group)
        return user