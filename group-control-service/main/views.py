from django.shortcuts import render

def index(request):
    # 그룹 목록 보여주기
    if not request.user.is_authenticated:
        username = ""
        return render(request, 'main/main.html', {'username':username})
    else:
        user = request.user
        username = user.username
    return  render(request, 'main/main.html', {'username':username})

def createGroup(request):
    # 그룹 생성하기
    return

def joinGroup(request):
    # 그룹 참여하기
    return