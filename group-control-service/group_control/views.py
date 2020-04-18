from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from main.models import *
from .models import *
from .forms import *

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
    }
    return render(request, "group_control/index.html", dict)

def showQuest(request, pk):
    currGroup = Group.objects.get(id=pk)
    currJoin = Join.objects.get(group=currGroup, user=request.user)
    quest = Quest.objects.filter(join=currJoin)
    dict = {
        'quest':quest,
    }
    return render(request, 'group_control/quest.html', dict)

def showNotice(request, pk):
    currGroup = Group.objects.get(id=pk)
    notice = Notice.objects.filter(group=currGroup)
    dict = {
        'notice': notice,
    }
    return render(request, 'group_control/notice.html', dict)

def createSche(request, pk):
    # 일정 생성 기능
    # 호스트 기능
    if request.method == 'POST':
        print("create Schedule")
        form = ScheduleForm(request.POST)
        if form.is_valid():
            new_sche = form.save(commit=False)
            currGroup = Group.objects.get(id=pk)
            print(new_sche.title)
            Schedule.objects.create(title=new_sche.title, date=new_sche.date, time=new_sche.time, group=currGroup)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def shareReward(request):
    # 상금 분배하는 기능
    return

def modify(request):
    # 그룹 데이터 수정 기능
    # 호스트 기능
    return

def invite(request):
    # 초대 기능
    # 호스트 기능
    return

def retire(request):
    # 강제 퇴장 기능
    # 호스트 기능
    return


def createQuest(request, pk):
    # 과제 생성 기능
    # 호스트 기능
    if request.method == 'POST':
        form = QuestForm(request.POST)
        if form.is_valid():
            new_Que = form.save(commit=False)
            currGroup = Group.objects.get(id=pk)
            Quest.objects.create(title=new_sche.title, date=new_sche.date, time=new_sche.time, group=currGroup)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return

def createNote(request):
    # 공지 작성 기능
    # 호스트 기능
    return

def approveSub(request):
    # 과제 승인 기능
    # 호스트 기능
    return

def approveFinal(request):
    # 최종 목표 승인 기능
    # 이 기능 후 상금 분배
    # 호스트 기능
    return

def unjoin(request):
    # 탈퇴 기능
    # 멤버 기능
    return

def checkSche(request):
    # 일정 체크 기능
    # 멤버 기능
    return

def submitSub(request):
    # 과제 제출 기능
    # 멤버 기능
    return

def checkFinal(request):
    # 최종 목표 달성 기능
    # 멤버 기능
    return



