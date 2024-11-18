from django.shortcuts import render
from django.contrib.auth import login as auth_login,logout as auth_logout,authenticate
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request,"dashboard/home.html")

def login(request):
    return render(request,"dashboard/login.html")

def signup(request):
    return render(request,'dashboard/signup.html')
