from django import forms
from app1.models import UserProfile
from django.contrib.auth.models import User


class Form1(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username','email','password')

class Form2(forms.ModelForm):
    class Meta():
        model=UserProfile
        exclude=('user',)