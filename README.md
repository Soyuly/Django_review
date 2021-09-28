# 🦁 Django 로그인과 템플릿 상속

### 1. 템플릿 상속하기
> **템플릿 상속이란?** <br>
> html 문서 중 기본 뼈대가 되는 문서를 기본 템플릿으로 정하고, 이는 공통의 코드이므로 다른 문서에서 기본 템플릿의 코드가 필요하면 상속하여 가져다 쓰는 것. <br>
> **한마디로 중복된 코드를 관리하여 코드 간결화가 목적**
+ **config 폴더 내부에 teamplates 폴더를 만들고 nav.html 파일을 추가한 후 다음의 코드를 nav.html에 복붙 합니다.**<br>

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
                <span class="nav-link active"  aria-current="page" href="#">🦁</span>
              </li>


          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="
            {% if request.user.is_authenticated %}
            {% url 'home' user.id %} {% else %} {% url 'home_logout' %} {% endif %}">홈으로!</a>
          </li>
          
          {% if request.user.is_authenticated %}
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="{% url 'logout_backend' %}">로그아웃</a>
          </li>
          {% else %}
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="{% url 'login' %}">로그인</a>
          </li>
          {% endif %}

          {% if request.user.is_authenticated %}
          <li class="nav-item">
            <span class="nav-link" href="{% url 'signup' %}" style="color: blue;">{{user.grade}} {{user.major}} {{user.name}}님 환영합니다.</span>
          </li>
          {% else %}
          <li class="nav-item">
            <a class="nav-link" href="{% url 'signup' %}">회원가입</a>
          </li>

          
          {% endif %}
 
        </ul>

      </div>
    </div>
  </nav>
```
+ **Setting.py -> TEMPLATES -> DIRS부분에 'config/templates'에 'config/templates' 를 넣어줍니다.**
> DIRS 옵션은 Django가 템플릿들을 찾는 디렉토리 경로를 지정하는 것으로, 원래는 비어 있었는데 위의 경로를 넣어줌으로써 nav.html을 찾게 해줍니다.
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
+ **그 후 nav.html에 중복 시키기 위해서 맨 밑줄에 {% block content %} {% endblock %} 부분을 추가해줍니다.**
![image](https://user-images.githubusercontent.com/86656269/133916200-d7eb15f7-6036-4e05-9743-4aadf67aca50.png)

+ **작업이 끝났으면 runserver를 해서 화면이 정상적으로 뜨는지 확인해봅시다ㅎㅎ**
(잘 되시면 버튼 클릭해보세요!!)
![image](https://user-images.githubusercontent.com/86656269/133916455-360c5c74-04a5-49e9-b36c-66c742f353cb.png)

***

### 2. url 관리하기
> 프로젝트를 진행하다보면 만들어야 하는 url도 많아지고, 이로인해 가독성이 떨어질 수도 있습니다. <br>
> ** 그래서 저희는 각각의 앱마다 따로 urls.py를 만들어줘서 코드를 효율적으로 괸리해보겠습니다! **
#### ✔ urls.py 코드를 다시 치려면 오류도 많이 뜨고, 시간이 많이 걸리니 눈으로 보는걸로 대체 하겠습니다.
+ account 폴더에 urls.py 파일을 하나 생성하고, config/urls.py내용을 그대로 복붙 합니다!.<br>
``` python
from django.contrib import admin
from django.urls import path
from review import views

urlpatterns = [

]
```
#### 이때 까먹지말고 from review import views 에서 account를 현재 앱 이름으로 바꿔줘야합니다! 안 바꿔주면 해당 앱의 views.py에서 인식을 못합니다.
![image](https://user-images.githubusercontent.com/86656269/134496232-df5f31ec-888e-443d-baec-ae7b53fe4b5b.png)
+ 프로젝트에서 account에 추가한 urls.py를 인식하게 하기 위해서 기존에 있었던 찐 config/urls.py 파일에 들어가서 다음 코드를 추가합니다.
```python
path('', include('account.urls')),
``` 
> 다음 코드는 account 폴더에 있는 urls.py를 불러오는 명령어 입니다.<br>
> 앞에 ''는 경로인데, 만약에 account의 urls.py 에서 'login/'이라는 경로가 존재하면 http://127.0.0.1:8000/login이 되는거고,<br>
> 만약에 path('')가 아니라 path('test/')로 설정하고 account의 urls.py 에서 'login/'이라는 경로가 존재하면 들어가는 홈페이지는 http://127.0.0.1:8000/test/login이 되는원리 입니다.
> 하나 더 예를 들자면 path('likelion/')으로 하고 account의 urls.py 에서 'login/'이라는 경로가 존재하면 http://127.0.0.1:8000/likelion/login이 됩니다.
***
### 3-1. 회원가입 구현하기(★★★)
> 기존에는 장고에서 기본적으로 제공하는 회원가입 폼을 사용해서 만드는걸 배웠는데습니다. 하지만 프로젝트를 진행하면서 CSS를 반강제적으로 넣게 되는데
> 폼을 사용하면 css 적용하는데 한계가 있으므로, 저희가 이쁘게 css로 꾸민 회원가입 홈페이지에서 직접 회원가입 폼을 적용시켜보겠습니다. <br>
> **Django 공식문서와 specy 프로젝트할 때, 가은이가 회원가입/로그인 구현했던 코드들을 참고 하였습니당**
#### ⚠ 시간 단축과 편의를 위해 urls.py 작성 과정이 생략 되어 있습니다. 
+ **account앱에 models.py는 없애면 시간이 많이 걸려서 사전에 작성 시켰는데 한번 분석 해봅시다!**
    + user에서 1:1관계 필드는 저도 데이터베이스를 안배워서 잘 이해를 못했는데, 밑에 인용구를 통해 어느정도 이해했습니다.
    + 나머지 name, grade, major 필드는 프로젝트를 만들다가 입맛에 맞게 만드시면 됩니다
> 예를 들어 1명의 유저는 하나의 프로필만을 가져야 한다고 강제한다면, one-to-one을 사용할 수 있다.
첫번째 테이블이 User, 두번째 테이블은 Profile이다. 두번째 테이블은 반드시 첫번째 테이블과 한번만 매칭된다.
지금 당장 One-to-one 모델에 대해 이해하지 못했다고 해서 걱정할 필요 없다고 조언한다. 흔하게 찾아볼 수 있는 관계도 아니거니와 특정 문제에 맞닥 뜨리면 찾아보게 된다고 한다..

```python
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
```
+ **account/views.py에 들어가서 다음을 import 해줍니다.
```python
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
```
+ **account/views.py에 들어가서 본격적으로 SignUp을 구현하기 위해 signup_backend 함수부분에 아래코드를 복사해서 붙여놓습니다.**
```python
def signup_backend(request):
    account = Account()
    account.name = request.POST['name']
    account.grade = request.POST['grade']
    account.major = request.POST['major']

    account.user = User.objects.create_user(
        username=request.POST['id'], password=request.POST['password'])

    account.save()
    
    #로그인 과정
    user = auth.authenticate(
    request, username=request.POST['id'], password=request.POST['password'])
    

    if account is not None:
        auth.login(request, user)
        return redirect('/home/'+str(request.user.id))
    else:
        error = 1
        return render(request,'login.html',{'error':error})
 ```
 + **코드분석**
    + 위의 account.name grade major은 signup.html의 인풋박스에서 값을 입력 받기 위해 적어놨습니다.(CRUD랑 똑같은 원리라 생략 하겠습니다.)
    + User.objects.create_user은 django 공식 문서에서 설명이 되어있듯이, 회원가입을 하는 가장 직접적인 방법은 create_user 메소드를 사용하는 것이라고 명시 되어있습니다.
     ![image](https://user-images.githubusercontent.com/86656269/133917192-246f886a-f3c1-438b-a260-8dd787bd91c8.png)
    + 즉, 새로운 유저를 만드는 메소드 입니다. 그래서 username, password 각각 인풋박스에서 불러온 값을 기반으로 아이디 비밀번호를 생성하고 이를 토대로 새로운 계정을 생성해줍니다.
    + 이후 authenticate(인증) 과정을 통해서 계정이 존재하면 auth.login(request, user) 로그인을 시도합니다.
    ![image](https://user-images.githubusercontent.com/86656269/133917512-c9624f80-b516-43a7-ab06-ae5339a9c8c2.png)

> 부가적으로 urls.py에서 signup_backend를 실행 시키기 위해 작성시키고, 이러한 url을 form태그에 적용하는 과정이 생략 되어 있습니다. 코드 보시면 쉽게 아실 수 있을겁니다!!

### 3-2. 로그인 구현하기(★★)
+ **account/views.py에 들어가서 본격적으로 로그인을 구현하기 위해 login_backend 함수부분에 아래코드를 복사해서 붙여놓습니다.**
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
+ signup_backend에서 설명한 것과 코드 똑같습니다!

+ 이제 로그인과 회원가입 백엔드가 완성이 되었으니 한번 테스트를 해봅시다!
![image](https://user-images.githubusercontent.com/86656269/133918073-601ba919-bb42-45b0-9bf9-9de1465dc3b9.png)
###### 이렇게 나오면 성공!

### 3-3. 로그아웃 구현하기(★)
+ **account/views.py에 들어가서 본격적으로 로그인을 구현하기 위해 logout_backend 함수부분에 아래코드를 복사해서 붙여놓습니다.**
``` python
def logout_backend(request):
    auth.logout(request)
    return redirect('home_logout')
```
###### 완전 간단합니다~ 로그아웃에 관한 django 공식 문서 참고하세요!
![image](https://user-images.githubusercontent.com/86656269/133918247-300a0cbe-55df-4b00-b3a0-d8deb6f57a47.png)

> 참고하면 유용한 문서 https://docs.djangoproject.com/en/3.2/topics/auth/default/

### 👏 감사합니다!! 모두 고생 하셨습니다~~
