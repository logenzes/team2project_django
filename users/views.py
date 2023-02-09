from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
# 로그인
def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        username = request.POST['userid']
        passwrd = request.POST['passwrd']
        print(username, passwrd)
        user = authenticate(request, username=username, password=passwrd)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('mypage:myGameScoreList'))
        else:
            return render(request, "login.html", {'error':'check_info', 'form':{'userid':username}})

# 회원가입
def register(request):
    print(request)
    if request.user.is_authenticated:
        return render(request, "login.html")
    if request.method == "POST":
        print(request.POST)
        userid = request.POST['userid']
        passwrd = request.POST['passwrd']
        passwrd_chk = request.POST['passwrd_chk']
        email = request.POST['email']
        user = User.objects.filter(username=userid)
        if len(user) > 0:
            context = {'form': request.POST, 'error':'id'}
            return render(request, "register.html", context)
        if passwrd == passwrd_chk:
            User.objects.create_user(
                username = userid,
                password = passwrd,
                email = email,
            )
            return HttpResponseRedirect(reverse('users:login'))
        else:
            # context = {'userid':userid, 'passwrd':passwrd, 'email':email}
            context = {'form': request.POST}
            return render(request, "register.html", context)

    return render(request, "register.html")

# log out
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('users:login'))

