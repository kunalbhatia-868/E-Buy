from django.contrib import auth
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import redirect, render

from users.models import UserProfile
from .forms import SignUpForm
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.


def signup(request):
    if request.method=='POST':
        form=SignUpForm(data=request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('login')
        else:
            messages.error(request,f"Please Enter Valid Information")
    else:
        form=SignUpForm()

    context={
        'form':form,
    }
    return render(request,"users/signup.html",context)


def logoutview(request):
    if not request.user:
        return redirect('login')
    else:
        logout(request)
        return redirect('home')


def loginview(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,f"You have been Logged in - {user.username}")
            return redirect('home')
        else:
            messages.error(request,f'please enter valid credentials')
    return render(request,'users/login.html')      

##################################################
##################################################
# HTMX check functions


def uniqueUsername(request):
    username=request.POST.get('username')
    if UserProfile.objects.filter(username=username).exists():
        return HttpResponse("<div class='error' id='username_text'>This username already exists</div>")

    else:
        return HttpResponse("<div class='success' id='username_text'>This username is available</div>") 

