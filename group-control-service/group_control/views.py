from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from main.models import *
from .models import *
from .forms import *
from django.utils.safestring import mark_safe
import json

def showGroup(request, pk):
    # 그룹에 관한 데이터를 보여주는 기능
    # 일정을 달력과 리스트의 형태로 표시
    # 개인의 능력치를 수치나 그래프로 표시
    # 각 멤버의 성과를 그래프로 표시
    # 공지 표시
    # 과제 표시
    currGroup = Group.objects.get(id=pk)
    currJoin = Join.objects.get(group=currGroup, user=request.user)
    schedules = Schedule.objects.filter(group=currGroup)
    user = request.user

    notices = Notice.objects.filter(group=currGroup)
    quests = Quest.objects.filter(join=currJoin)
    sche_form = ScheduleForm()
    questCount = len(quests)
    schedule = schedules[0:2]
    quest = quests[0:3]
    notice = notices[0:2]
    dict = {
        'group':currGroup,
        'join':currJoin,
        'schedule':schedule,
        'notice':notice,
        'quest': quest,
        'questCount': questCount,
        'sche_form': sche_form,
        'user': user,
    }
    return render(request, "group_control/index.html", dict)

def showQuest(request, pk):
    currGroup = Group.objects.get(id=pk)
    currJoin = Join.objects.get(group=currGroup, user=request.user)
    quest = Quest.objects.filter(join=currJoin)
    form = QuestForm()
    dict = {
        'group': currGroup,
        'quest':quest,
        'form':form,
    }
    return render(request, 'group_control/quest.html', dict)

def showNotice(request, pk):
    currGroup = Group.objects.get(id=pk)
    notice = Notice.objects.filter(group=currGroup)
    form = NoticeForm()
    dict = {
        'group': currGroup,
        'notice': notice,
        'form': form,
    }
    return render(request, 'group_control/notice.html', dict)

def createSche(request, pk):
    # 일정 생성 기능
    # 호스트 기능
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            new_sche = form.save(commit=False)
            currGroup = Group.objects.get(id=pk)
            Schedule.objects.create(title=new_sche.title, date=new_sche.date, time=new_sche.time, group=currGroup)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def createQuest(request, pk):
    # 과제 생성 기능
    # 호스트 기능
    if request.method == 'POST':
        form = QuestForm(request.POST)
        if form.is_valid():
            newQue = form.save(commit=False)
            currGroup = Group.objects.get(id=pk)
            currJoin = Join.objects.get(group=currGroup, user=request.user)
            Quest.objects.create(title=newQue.title, type=newQue.type, exp=newQue.exp, end=newQue.end, join=currJoin, content=newQue.content)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def createNotice(request, pk):
    # 공지 작성 기능
    # 호스트 기능
    if request.method == 'POST':
        print("createQuest!")
        form = NoticeForm(request.POST)
        if form.is_valid():
            newNot = form.save(commit=False)
            currGroup = Group.objects.get(id=pk)
            Notice.objects.create(title=newNot.title, type=newNot.type, content=newNot.content, group=currGroup)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def showChat(request, pk):
    group = Group.objects.get(id=pk)        # 그룹 데이터
    join = Join.objects.filter(group=group)    # 그룹에 참여한 유저 데이터
    dict = {
        'group': group,
        'join': join,
    }
    return render(request, 'group_control/chat.html', dict)

def createChat(request, pk):
    return


