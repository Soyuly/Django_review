"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from account import views

urlpatterns = [
    path('login',views.login, name='login'),
    path('login_backend', views.login_backend, name='login_backend'),
    path('logoug_backend', views.logout_backend, name='logout_backend'),
    path('signup',views.signup, name='signup'),
    path('signup_backend', views.signup_backend, name='signup_backend'),
]
