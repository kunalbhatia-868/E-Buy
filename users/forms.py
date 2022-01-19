from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','autocomplete':'off', 'placeholder': 'Username','hx-post':'/users/check-username/','hx-trigger':'keyup delay:1s changed','hx-target':'#username_text','hx-swap':'outerHTML'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), max_length=32)
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), max_length=32)
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), max_length=64)
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),label="Password")
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),label="Confirm Password")
    class Meta:
        model=UserProfile
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')