from django.shortcuts import render

def login_check(request):
    return render(request, 'accounts/index.html')

def logout(request):
    # 로그아웃
    return

def signup(request):
    # 회원가입
    return

def findPw(request):
    # 비밀번호 찾기
    return


