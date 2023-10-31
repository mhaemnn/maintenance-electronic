from django.contrib.auth.forms import UserCreationForm, get_user_model
from django.contrib.auth.models import User
from django import forms


# login / register
class CreateUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']
