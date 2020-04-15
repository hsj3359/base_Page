from django.shortcuts import render
from .models import Group, Join

def index(request):
    # 그룹 목록 보여주기
    if not request.user.is_authenticated:
        username = ""
        return render(request, 'main/main.html', {'username':username})
    else:
        username = request.user.username
        join = Join.objects.filter(user=request.user)
        dict = {
            'username':username,
            'join':join
        }
    return  render(request, 'main/main.html', dict)

def createGroup(request):
    # 그룹 생성하기
    return

def joinGroup(request):
    # 그룹 참여하기
    return