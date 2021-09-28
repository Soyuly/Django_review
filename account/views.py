from django.shortcuts import render,redirect
from .models import Account

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
