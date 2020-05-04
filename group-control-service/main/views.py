from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
import random

def index(request):
    if not request.user.is_authenticated:
        username = ""
        return render(request, 'main/main.html', {'username':username})
    else:
        user = request.user
        join = Join.objects.filter(user=request.user)
        createGroupForm = CreateGroupForm()
        joinGroupForm = JoinGroupForm()
        dict = {
            'user':user,
            'join':join,
            'createGroupForm':createGroupForm,
            'joinGroupForm':joinGroupForm,
        }
    return  render(request, 'main/main.html', dict)

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
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def joinGroup(request):
    # 그룹 참여하기
    if request.method == 'POST':
        user = request.user
        form = JoinGroupForm(request.POST)
        if form.is_valid():
            code = form.save(commit=False)
            studyGroup = StudyGroup.objects.get(code=code.code)
            studyGroup.save()
            Join.objects.create(user=user, studyGroup=studyGroup)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))