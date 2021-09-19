from django.shortcuts import render,redirect
from .models import Account
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    return render(request,'login.html')


def login_backend(request):
    username = request.POST['id']
    password = request.POST['password']
    user = auth.authenticate(request, username=username, password=password)
    if user is not None:
        auth.login(request, user)
        
        return redirect('home/'+str(request.user.id))
    else:
        error = 1
        return render(request,'login.html',{'error':error})

def logout_backend(request):
    auth.logout(request)
    return redirect('home_logout')

def signup(request):
    return render(request,'signup.html')

def signup_backend(request):
    account = Account()
    account.name = request.POST['name']
    account.grade = request.POST['grade']
    account.major = request.POST['major']

    account.user = User.objects.create_user(
        username=request.POST['id'], password=request.POST['password'])

    account.save()
    print('회원가입')
    user = auth.authenticate(
    request, username=request.POST['id'], password=request.POST['password'])

    if account is not None:
        auth.login(request, user)
        return redirect('/home/'+str(request.user.id))
    else:
        error = 1
        return render(request,'login.html',{'error':error})