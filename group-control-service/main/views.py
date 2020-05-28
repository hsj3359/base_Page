from django.shortcuts import render
from django.http import HttpResponseRedirect
from group_control.models import Schedule
from .models import *
from .forms import *
import random

# main.html
def index(request):
    user = ""
    if not request.user.is_authenticated:
        return render(request, 'main/main.html', {'user':user})
    else:
        user = request.user
        join = Join.objects.filter(user=request.user)
        createGroupForm = CreateGroupForm()
        joinGroupForm = JoinGroupForm()
        schedule = Schedule.objects.filter(user=request.user)
        dict = {
            'user': user,
            'join': join,
            'createGroupForm': createGroupForm,
            'joinGroupForm': joinGroupForm,
            'schedule': schedule,
        }
    return  render(request, 'main/main.html', dict)

# 그룹 생성
def createGroup(request):
    if request.method == 'POST':
        form = CreateGroupForm(request.POST)
        user = request.user
        if form.is_valid():
            studyGroup = form.save(commit=False)
            studyGroup.host = user
            studyGroup.code = random.randint(0, 9999)
            studyGroup.save()
            Join.objects.create(user=user, studyGroup=studyGroup)
            print("Success create Group!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# 그룹 참여하기
def joinGroup(request):
    if request.method == 'POST':
        user = request.user
        form = JoinGroupForm(request.POST)
        if form.is_valid():
            code = form.save(commit=False)
            studyGroup = StudyGroup.objects.get(code=code.code)
            studyGroup.save()
            Join.objects.create(user=user, studyGroup=studyGroup)
            print("Success join Group!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
