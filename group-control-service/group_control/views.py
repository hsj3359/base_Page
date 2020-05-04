from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from main.models import StudyGroup, Join
from .models import *
from .forms import *

def showGroup(request, pk):
    # 그룹에 관한 데이터를 보여주는 기능
    # 일정을 달력과 리스트의 형태로 표시
    # 개인의 능력치를 수치나 그래프로 표시
    # 각 멤버의 성과를 그래프로 표시
    # 공지 표시
    # 과제 표시
    studyGroup = StudyGroup.objects.get(id=pk)
    join = Join.objects.get(user=request.user, studyGroup=studyGroup)
    schedules = Schedule.objects.filter(studyGroup=studyGroup)
    user = request.user
    notices = Notice.objects.filter(studyGroup=studyGroup)
    scheForm = ScheduleForm()
    schedule = schedules[0:2]
    notice = notices[0:2]
    dict = {
        'group':studyGroup,
        'join':join,
        'schedule':schedule,
        'notice':notice,
        'sche_form': scheForm,
        'user': user,
    }
    return render(request, "group_control/index.html", dict)

def showNotice(request, pk):
    studyGroup = StudyGroup.objects.get(id=pk)
    notice = Notice.objects.filter(studyGroup=studyGroup)
    form = NoticeForm()
    dict = {
        'group': studyGroup,
        'notice': notice,
        'form': form,
    }
    return render(request, 'group_control/notice.html', dict)

def createSche(request, pk):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            new_sche = form.save(commit=False)
            studyGroup = StudyGroup.objects.get(id=pk)
            Schedule.objects.create(title=new_sche.title, date=new_sche.date, time=new_sche.time, studyGroup=studyGroup)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def createNotice(request, pk):
    if request.method == 'POST':
        print("createQuest!")
        form = NoticeForm(request.POST)
        if form.is_valid():
            newNot = form.save(commit=False)
            studyGroup = StudyGroup.objects.get(id=pk)
            Notice.objects.create(title=newNot.title, type=newNot.type, content=newNot.content, studyGroup=studyGroup)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def showChat(request, pk):
    studyGroup = StudyGroup.objects.get(id=pk)        # 그룹 데이터
    join = Join.objects.filter(studyGroup=studyGroup)    # 그룹에 참여한 유저 데이터
    dict = {
        'group': studyGroup,
        'join': join,
    }
    return render(request, 'group_control/chat.html', dict)

def showBook(request, pk):
    studyGroup = StudyGroup.objects.get(id=pk)
    dict = {
        'group': studyGroup,
    }
    return render(request, 'group_control/book.html', dict)



