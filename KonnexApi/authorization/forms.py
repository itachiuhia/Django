from django import forms
from django.contrib.auth.models import User
from .models import User_Profile
from django.contrib.auth.forms import UserCreationForm



# class UserRegistrationForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta :
#         model = User
#         fields = ('username','email', 'password1', 'password2')


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = ['username','email', 'password1', 'password2']