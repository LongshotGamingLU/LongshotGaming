from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from User.models import LongshotUser
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        
class LongshotUserForm(forms.ModelForm):
    class Meta:
        model = LongshotUser
        fields = ('userId',)