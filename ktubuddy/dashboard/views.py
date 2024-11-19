from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import login as auth_login,logout as auth_logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"dashboard/home.html")

def login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request=request,username=username,password=password)
        if user:
            auth_login(request=request,user=user)
            return redirect('home')
        else:
            return HttpResponse("error logging in")
    return render(request,"dashboard/login.html")

def signup(request):
    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        re_password=request.POST.get("password")
        if password==re_password:
            user=User.objects.create_user(username,email,password)
            user.save()
            if user is None:
                            return HttpResponse("error logging in")
            return redirect("login")
        else:
            return HttpResponse("passwords dont match")
    return render(request,'dashboard/signup.html')
def logout(request):
     if request.method=="POST":
          auth_logout(request)
          return redirect('home')
