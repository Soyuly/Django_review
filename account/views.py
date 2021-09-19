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
    #로그인 백엔드 구현하는 공간
    print('코드 입력 부분입니다! print문 지우고 입력해주세요~')

def logout_backend(request):
    #로그아웃 백엔드 구현하는 공간
    print('코드 입력 부분입니다! print문 지우고 입력해주세요~')

def signup(request):
    return render(request,'signup.html')

def signup_backend(request):
    #회원가입 백엔드 구현하는 공간
    print('코드 입력 부분입니다! print문 지우고 입력해주세요~')