from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import  logout as django_logout
from django.contrib.auth.models import User
from .forms import ReigsterForm

def login_check(request):
    # 로그인
    if request.method == "POST":
        name = request.POST.get('username', '')
        pwd = request.POST.get('password', '')
        user = authenticate(username=name, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('main:index')
        else:
            return render(request, 'accounts/login.html')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    # 로그아웃
    django_logout(request)
    return redirect("/")

def register(request):
    # 회원가입
    if request.method == 'POST':
        form = ReigsterForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["password"] == request.POST["password2"]:
                user = User.objects.create_user(**form.cleaned_data)
                return redirect('accounts:login')
    else:
        form = ReigsterForm()
    return render(request, 'accounts/register.html', {'form':form})

def forgot_password(request):
    # 비밀번호 찾기
    return render(request, 'accounts/forgot-password.html')


