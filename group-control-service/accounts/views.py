from django.shortcuts import render

def login_check(request):
    return render(request, 'accounts/index.html')
