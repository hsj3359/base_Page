from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
import random

def index(request):
    # 그룹 목록 보여주기
    if not request.user.is_authenticated:
        username = ""
        return render(request, 'main/main.html', {'username':username})
    else:
        user = request.user
        join = Join.objects.filter(user=request.user)
        groupForm = GroupForm()
        joinForm = JoinForm()
        li = []
        for j in join:
            li.append(Join.objects.filter(group=j.group).count())
        length = join.count()
        dict = {
            'user':user,
            'join':join,
            'groupForm':groupForm,
            'joinForm':joinForm,
            'li':li,
            'length':length,
        }
    return  render(request, 'main/main.html', dict)

def createGroup(request):
    # 그룹 생성하기
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.host = request.user
            group.code = random.randint(0, 9999)
            group.save()
            Join.objects.create(user=group.host, group=group)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def joinGroup(request):
    # 그룹 참여하기
    if request.method == 'POST':
        user = request.user
        form = JoinForm(request.POST)
        if form.is_valid():
            code = form.save(commit=False)
            group = Group.objects.get(code=code.code)
            group.count = group.count + 1
            group.save()
            Join.objects.create(user=user, group=group)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))