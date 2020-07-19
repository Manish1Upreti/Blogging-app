from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# UserRegisterForm class  is inherit from UserCreationForm
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

# This class Meta gives nested name for the configuration
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name',  'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
        email = forms.EmailField()

        class Meta:
            model = User
            fields = ['username', 'email', 'first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):
        class Meta:
            model = Profile
            fields = ['image']