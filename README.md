# ๐ฆ Django ๋ก๊ทธ์ธ๊ณผ ํํ๋ฆฟ ์์

### 1. ํํ๋ฆฟ ์์ํ๊ธฐ
> **ํํ๋ฆฟ ์์์ด๋?** <br>
> html ๋ฌธ์ ์ค ๊ธฐ๋ณธ ๋ผ๋๊ฐ ๋๋ ๋ฌธ์๋ฅผ ๊ธฐ๋ณธ ํํ๋ฆฟ์ผ๋ก ์ ํ๊ณ , ์ด๋ ๊ณตํต์ ์ฝ๋์ด๋ฏ๋ก ๋ค๋ฅธ ๋ฌธ์์์ ๊ธฐ๋ณธ ํํ๋ฆฟ์ ์ฝ๋๊ฐ ํ์ํ๋ฉด ์์ํ์ฌ ๊ฐ์ ธ๋ค ์ฐ๋ ๊ฒ. <br>
> **ํ๋ง๋๋ก ์ค๋ณต๋ ์ฝ๋๋ฅผ ๊ด๋ฆฌํ์ฌ ์ฝ๋ ๊ฐ๊ฒฐํ๊ฐ ๋ชฉ์ **
+ **config ํด๋ ๋ด๋ถ์ teamplates ํด๋๋ฅผ ๋ง๋ค๊ณ  nav.html ํ์ผ์ ์ถ๊ฐํ ํ ๋ค์์ ์ฝ๋๋ฅผ nav.html์ ๋ณต๋ถ ํฉ๋๋ค.**<br>

```html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <a class="navbar-brand" href="#"></a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        
            <li class="nav-item">
                <span class="nav-link active"  aria-current="page" href="#">๐ฆ</span>
              </li>


          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="
            {% if request.user.is_authenticated %}
            {% url 'home' user.id %} {% else %} {% url 'home_logout' %} {% endif %}">ํ์ผ๋ก!</a>
          </li>
          
          {% if request.user.is_authenticated %}
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="{% url 'logout_backend' %}">๋ก๊ทธ์์</a>
          </li>
          {% else %}
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="{% url 'login' %}">๋ก๊ทธ์ธ</a>
          </li>
          {% endif %}

          {% if request.user.is_authenticated %}
          <li class="nav-item">
            <span class="nav-link" href="{% url 'signup' %}" style="color: blue;">{{user.grade}} {{user.major}} {{user.name}}๋ ํ์ํฉ๋๋ค.</span>
          </li>
          {% else %}
          <li class="nav-item">
            <a class="nav-link" href="{% url 'signup' %}">ํ์๊ฐ์</a>
          </li>

          
          {% endif %}
 
        </ul>

      </div>
    </div>
  </nav>
```
+ **Setting.py -> TEMPLATES -> DIRS๋ถ๋ถ์ 'config/templates'์ 'config/templates' ๋ฅผ ๋ฃ์ด์ค๋๋ค.**
> DIRS ์ต์์ Django๊ฐ ํํ๋ฆฟ๋ค์ ์ฐพ๋ ๋๋ ํ ๋ฆฌ ๊ฒฝ๋ก๋ฅผ ์ง์ ํ๋ ๊ฒ์ผ๋ก, ์๋๋ ๋น์ด ์์๋๋ฐ ์์ ๊ฒฝ๋ก๋ฅผ ๋ฃ์ด์ค์ผ๋ก์จ nav.html์ ์ฐพ๊ฒ ํด์ค๋๋ค.
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['config/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
+ **๊ทธ ํ nav.html์ ์ค๋ณต ์ํค๊ธฐ ์ํด์ ๋งจ ๋ฐ์ค์ {% block content %} {% endblock %} ๋ถ๋ถ์ ์ถ๊ฐํด์ค๋๋ค.**
![image](https://user-images.githubusercontent.com/86656269/133916200-d7eb15f7-6036-4e05-9743-4aadf67aca50.png)

+ **์ด์  ๋ค๋น๋ฐ ์ ์ฉ์ ์ํ๋ ํํ์ด์ง์ ๋ค์ด๊ฐ์ ๋ค๋น๋ฐ ์ฆ ์๊น๋ง๋  ํํ๋ฆฟ์ ์ ์ฉ์์ผ๋ณด๊ฒ ์ต๋๋ค.**<br>
>  **review/templates/home.html์ ๋ค์ด๊ฐ์ {% extends 'nav.html' %}์ ๋ฌด์กฐ๊ฑด ์ ์ผ ์ฒซ์ค์ ์ ์ด ์ค๋๋ค.**<br>
  **์ดํ ๋ง์ง๋ง ์ค์ {% endblock %}์ ์ ์ด์ค์ผ๋ก์จ ํํ๋ฆฟ ์์์ ์์ผ์ค๋๋ค**
  
![image](https://user-images.githubusercontent.com/86656269/135008212-2486b1c8-cef7-4e39-b2b0-c5a08cea55dd.png)

+ **์์์ด ๋๋ฌ์ผ๋ฉด runserver๋ฅผ ํด์ ํ๋ฉด์ด ์ ์์ ์ผ๋ก ๋จ๋์ง ํ์ธํด๋ด์๋คใใ**
(์ ๋์๋ฉด ๋ฒํผ ํด๋ฆญํด๋ณด์ธ์!!)
![image](https://user-images.githubusercontent.com/86656269/133916455-360c5c74-04a5-49e9-b36c-66c742f353cb.png)

***

### 2. url ๊ด๋ฆฌํ๊ธฐ
> ํ๋ก์ ํธ๋ฅผ ์งํํ๋ค๋ณด๋ฉด ๋ง๋ค์ด์ผ ํ๋ url๋ ๋ง์์ง๊ณ , ์ด๋ก์ธํด ๊ฐ๋์ฑ์ด ๋จ์ด์ง ์๋ ์์ต๋๋ค. <br>
> **๊ทธ๋์ ์ ํฌ๋ ๊ฐ๊ฐ์ ์ฑ๋ง๋ค ๋ฐ๋ก urls.py๋ฅผ ๋ง๋ค์ด์ค์ ์ฝ๋๋ฅผ ํจ์จ์ ์ผ๋ก ๊ด๋ฆฌํด๋ณด๊ฒ ์ต๋๋ค!**
#### โ urls.py ์ฝ๋๋ฅผ ๋ค์ ์น๋ ค๋ฉด ์ค๋ฅ๋ ๋ง์ด ๋จ๊ณ , ์๊ฐ์ด ๋ง์ด ๊ฑธ๋ฆฌ๋ ๋์ผ๋ก ๋ณด๋๊ฑธ๋ก ๋์ฒด ํ๊ฒ ์ต๋๋ค.
+ account ํด๋์ urls.py ํ์ผ์ ํ๋ ์์ฑํ๊ณ , config/urls.py๋ด์ฉ์ ๊ทธ๋๋ก ๋ณต๋ถ ํฉ๋๋ค!.<br>
``` python
from django.contrib import admin
from django.urls import path
from review import views

urlpatterns = [

]
```
#### ์ด๋ ๊น๋จน์ง๋ง๊ณ  from review import views ์์ account๋ฅผ ํ์ฌ ์ฑ ์ด๋ฆ์ผ๋ก ๋ฐ๊ฟ์ค์ผํฉ๋๋ค! ์ ๋ฐ๊ฟ์ฃผ๋ฉด ํด๋น ์ฑ์ views.py์์ ์ธ์์ ๋ชปํฉ๋๋ค.
![image](https://user-images.githubusercontent.com/86656269/134496232-df5f31ec-888e-443d-baec-ae7b53fe4b5b.png)
+ ํ๋ก์ ํธ์์ account์ ์ถ๊ฐํ urls.py๋ฅผ ์ธ์ํ๊ฒ ํ๊ธฐ ์ํด์ ๊ธฐ์กด์ ์์๋ ์ฐ config/urls.py ํ์ผ์ ๋ค์ด๊ฐ์ ๋ค์ ์ฝ๋๋ฅผ ์ถ๊ฐํฉ๋๋ค.
```python
path('', include('account.urls')),
``` 
> ๋ค์ ์ฝ๋๋ account ํด๋์ ์๋ urls.py๋ฅผ ๋ถ๋ฌ์ค๋ ๋ช๋ น์ด ์๋๋ค.<br>
> ์์ ''๋ ๊ฒฝ๋ก์ธ๋ฐ, ๋ง์ฝ์ account์ urls.py ์์ 'login/'์ด๋ผ๋ ๊ฒฝ๋ก๊ฐ ์กด์ฌํ๋ฉด http://127.0.0.1:8000/login์ด ๋๋๊ฑฐ๊ณ ,<br>
> ๋ง์ฝ์ path('')๊ฐ ์๋๋ผ path('test/')๋ก ์ค์ ํ๊ณ  account์ urls.py ์์ 'login/'์ด๋ผ๋ ๊ฒฝ๋ก๊ฐ ์กด์ฌํ๋ฉด ๋ค์ด๊ฐ๋ ํํ์ด์ง๋ http://127.0.0.1:8000/test/login์ด ๋๋์๋ฆฌ ์๋๋ค.
> ํ๋ ๋ ์๋ฅผ ๋ค์๋ฉด path('likelion/')์ผ๋ก ํ๊ณ  account์ urls.py ์์ 'login/'์ด๋ผ๋ ๊ฒฝ๋ก๊ฐ ์กด์ฌํ๋ฉด http://127.0.0.1:8000/likelion/login์ด ๋ฉ๋๋ค.
***
### 3-1. ํ์๊ฐ์ ๊ตฌํํ๊ธฐ(โโโ)
> ๊ธฐ์กด์๋ ์ฅ๊ณ ์์ ๊ธฐ๋ณธ์ ์ผ๋ก ์ ๊ณตํ๋ ํ์๊ฐ์ ํผ์ ์ฌ์ฉํด์ ๋ง๋๋๊ฑธ ๋ฐฐ์ ๋๋ฐ์ต๋๋ค. ํ์ง๋ง ํ๋ก์ ํธ๋ฅผ ์งํํ๋ฉด์ CSS๋ฅผ ๋ฐ๊ฐ์ ์ ์ผ๋ก ๋ฃ๊ฒ ๋๋๋ฐ
> ํผ์ ์ฌ์ฉํ๋ฉด css ์ ์ฉํ๋๋ฐ ํ๊ณ๊ฐ ์์ผ๋ฏ๋ก, ์ ํฌ๊ฐ ์ด์๊ฒ css๋ก ๊พธ๋ฏผ ํ์๊ฐ์ ํํ์ด์ง์์ ์ง์  ํ์๊ฐ์ ํผ์ ์ ์ฉ์์ผ๋ณด๊ฒ ์ต๋๋ค. <br>
> **Django ๊ณต์๋ฌธ์์ specy ํ๋ก์ ํธํ  ๋, ๊ฐ์์ด๊ฐ ํ์๊ฐ์/๋ก๊ทธ์ธ ๊ตฌํํ๋ ์ฝ๋๋ค์ ์ฐธ๊ณ  ํ์์ต๋๋น**
#### โ  ์๊ฐ ๋จ์ถ๊ณผ ํธ์๋ฅผ ์ํด urls.py ์์ฑ ๊ณผ์ ์ด ์๋ต ๋์ด ์์ต๋๋ค. 
+ **account์ฑ์ models.py๋ ์์ ๋ฉด ์๊ฐ์ด ๋ง์ด ๊ฑธ๋ ค์ ์ฌ์ ์ ์์ฑ ์์ผฐ๋๋ฐ ํ๋ฒ ๋ถ์ ํด๋ด์๋ค!**
    + user์์ 1:1๊ด๊ณ ํ๋๋ ์ ๋ ๋ฐ์ดํฐ๋ฒ ์ด์ค๋ฅผ ์๋ฐฐ์์ ์ ์ดํด๋ฅผ ๋ชปํ๋๋ฐ, ๋ฐ์ ์ธ์ฉ๊ตฌ๋ฅผ ํตํด ์ด๋์ ๋ ์ดํดํ์ต๋๋ค.
    + ๋๋จธ์ง name, grade, major ํ๋๋ ํ๋ก์ ํธ๋ฅผ ๋ง๋ค๋ค๊ฐ ์๋ง์ ๋ง๊ฒ ๋ง๋์๋ฉด ๋ฉ๋๋ค
> ์๋ฅผ ๋ค์ด 1๋ช์ ์ ์ ๋ ํ๋์ ํ๋กํ๋ง์ ๊ฐ์ ธ์ผ ํ๋ค๊ณ  ๊ฐ์ ํ๋ค๋ฉด, one-to-one์ ์ฌ์ฉํ  ์ ์๋ค.
์ฒซ๋ฒ์งธ ํ์ด๋ธ์ด User, ๋๋ฒ์งธ ํ์ด๋ธ์ Profile์ด๋ค. ๋๋ฒ์งธ ํ์ด๋ธ์ ๋ฐ๋์ ์ฒซ๋ฒ์งธ ํ์ด๋ธ๊ณผ ํ๋ฒ๋ง ๋งค์นญ๋๋ค.
์ง๊ธ ๋น์ฅ One-to-one ๋ชจ๋ธ์ ๋ํด ์ดํดํ์ง ๋ชปํ๋ค๊ณ  ํด์ ๊ฑฑ์ ํ  ํ์ ์๋ค๊ณ  ์กฐ์ธํ๋ค. ํํ๊ฒ ์ฐพ์๋ณผ ์ ์๋ ๊ด๊ณ๋ ์๋๊ฑฐ๋์ ํน์  ๋ฌธ์ ์ ๋ง๋ฅ ๋จ๋ฆฌ๋ฉด ์ฐพ์๋ณด๊ฒ ๋๋ค๊ณ  ํ๋ค..

```python
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
```
+ **account/views.py์ ๋ค์ด๊ฐ์ ๋ค์์ import ํด์ค๋๋ค.**
```python
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
```
+ **account/views.py์ ๋ค์ด๊ฐ์ ๋ณธ๊ฒฉ์ ์ผ๋ก SignUp์ ๊ตฌํํ๊ธฐ ์ํด signup_backend ํจ์๋ถ๋ถ์ ์๋์ฝ๋๋ฅผ ๋ณต์ฌํด์ ๋ถ์ฌ๋์ต๋๋ค.**
```python
def signup_backend(request):
    account = Account()
    account.name = request.POST['name']
    account.grade = request.POST['grade']
    account.major = request.POST['major']

    account.user = User.objects.create_user(
        username=request.POST['id'], password=request.POST['password'])

    account.save()
    
    #๋ก๊ทธ์ธ ๊ณผ์ 
    user = auth.authenticate(
    request, username=request.POST['id'], password=request.POST['password'])
    

    if account is not None:
        auth.login(request, user)
        return redirect('/home/'+str(request.user.id))
    else:
        error = 1
        return render(request,'login.html',{'error':error})
 ```
 + **์ฝ๋๋ถ์**
    + ์์ account.name grade major์ signup.html์ ์ธํ๋ฐ์ค์์ ๊ฐ์ ์๋ ฅ ๋ฐ๊ธฐ ์ํด ์ ์ด๋จ์ต๋๋ค.(CRUD๋ ๋๊ฐ์ ์๋ฆฌ๋ผ ์๋ต ํ๊ฒ ์ต๋๋ค.)
    + User.objects.create_user์ django ๊ณต์ ๋ฌธ์์์ ์ค๋ช์ด ๋์ด์๋ฏ์ด, ํ์๊ฐ์์ ํ๋ ๊ฐ์ฅ ์ง์ ์ ์ธ ๋ฐฉ๋ฒ์ create_user ๋ฉ์๋๋ฅผ ์ฌ์ฉํ๋ ๊ฒ์ด๋ผ๊ณ  ๋ช์ ๋์ด์์ต๋๋ค.
     ![image](https://user-images.githubusercontent.com/86656269/133917192-246f886a-f3c1-438b-a260-8dd787bd91c8.png)
    + ์ฆ, ์๋ก์ด ์ ์ ๋ฅผ ๋ง๋๋ ๋ฉ์๋ ์๋๋ค. ๊ทธ๋์ username, password ๊ฐ๊ฐ ์ธํ๋ฐ์ค์์ ๋ถ๋ฌ์จ ๊ฐ์ ๊ธฐ๋ฐ์ผ๋ก ์์ด๋ ๋น๋ฐ๋ฒํธ๋ฅผ ์์ฑํ๊ณ  ์ด๋ฅผ ํ ๋๋ก ์๋ก์ด ๊ณ์ ์ ์์ฑํด์ค๋๋ค.
    + ์ดํ authenticate(์ธ์ฆ) ๊ณผ์ ์ ํตํด์ ๊ณ์ ์ด ์กด์ฌํ๋ฉด auth.login(request, user) ๋ก๊ทธ์ธ์ ์๋ํฉ๋๋ค.
    ![image](https://user-images.githubusercontent.com/86656269/133917512-c9624f80-b516-43a7-ab06-ae5339a9c8c2.png)

> ๋ถ๊ฐ์ ์ผ๋ก urls.py์์ signup_backend๋ฅผ ์คํ ์ํค๊ธฐ ์ํด ์์ฑ์ํค๊ณ , ์ด๋ฌํ url์ formํ๊ทธ์ ์ ์ฉํ๋ ๊ณผ์ ์ด ์๋ต ๋์ด ์์ต๋๋ค. ์ฝ๋ ๋ณด์๋ฉด ์ฝ๊ฒ ์์ค ์ ์์๊ฒ๋๋ค!!

### 3-2. ๋ก๊ทธ์ธ ๊ตฌํํ๊ธฐ(โโ)
+ **account/views.py์ ๋ค์ด๊ฐ์ ๋ณธ๊ฒฉ์ ์ผ๋ก ๋ก๊ทธ์ธ์ ๊ตฌํํ๊ธฐ ์ํด login_backend ํจ์๋ถ๋ถ์ ์๋์ฝ๋๋ฅผ ๋ณต์ฌํด์ ๋ถ์ฌ๋์ต๋๋ค.**
``` python
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
```
+ signup_backend์์ ์ค๋ชํ ๊ฒ๊ณผ ์ฝ๋ ๋๊ฐ์ต๋๋ค!

+ ์ด์  ๋ก๊ทธ์ธ๊ณผ ํ์๊ฐ์ ๋ฐฑ์๋๊ฐ ์์ฑ์ด ๋์์ผ๋ ํ๋ฒ ํ์คํธ๋ฅผ ํด๋ด์๋ค!
![image](https://user-images.githubusercontent.com/86656269/133918073-601ba919-bb42-45b0-9bf9-9de1465dc3b9.png)
###### ์ด๋ ๊ฒ ๋์ค๋ฉด ์ฑ๊ณต!

### 3-3. ๋ก๊ทธ์์ ๊ตฌํํ๊ธฐ(โ)
+ **account/views.py์ ๋ค์ด๊ฐ์ ๋ณธ๊ฒฉ์ ์ผ๋ก ๋ก๊ทธ์ธ์ ๊ตฌํํ๊ธฐ ์ํด logout_backend ํจ์๋ถ๋ถ์ ์๋์ฝ๋๋ฅผ ๋ณต์ฌํด์ ๋ถ์ฌ๋์ต๋๋ค.**
``` python
def logout_backend(request):
    auth.logout(request)
    return redirect('home_logout')
```
###### ์์  ๊ฐ๋จํฉ๋๋ค~ ๋ก๊ทธ์์์ ๊ดํ django ๊ณต์ ๋ฌธ์ ์ฐธ๊ณ ํ์ธ์!
![image](https://user-images.githubusercontent.com/86656269/133918247-300a0cbe-55df-4b00-b3a0-d8deb6f57a47.png)

> ์ฐธ๊ณ ํ๋ฉด ์ ์ฉํ ๋ฌธ์ https://docs.djangoproject.com/en/3.2/topics/auth/default/

### ๐ ๊ฐ์ฌํฉ๋๋ค!! ๋ชจ๋ ๊ณ ์ ํ์จ์ต๋๋ค~~
