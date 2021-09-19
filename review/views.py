from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from account.models import Account
from django.contrib import auth

# Create your views here.
@login_required
def home(request, user_id):
    user = get_object_or_404(Account, pk=user_id)
    if request.user.is_authenticated:
        print('성공')
        return render(request,'home.html',{'user':user})

def home_logout(request):
    return render(request,'home.html')

