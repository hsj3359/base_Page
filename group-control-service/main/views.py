from django.shortcuts import render
from django.http import HttpResponseRedirect
from group_control.models import Schedule, Study
from .models import *
from .forms import *
import random
from datetime import datetime, timedelta

def index(request):
    if not request.user.is_authenticated:
        username = ""
        return render(request, 'main/main.html', {'username':username})
    else:
        user = request.user
        join = Join.objects.filter(user=request.user)
        createGroupForm = CreateGroupForm()
        joinGroupForm = JoinGroupForm()
        schedule = Schedule.objects.filter(user=request.user)
        checkDayStudy(user, schedule, join)
        dict = {
            'user':user,
            'join':join,
            'createGroupForm':createGroupForm,
            'joinGroupForm':joinGroupForm,
            'schedule':schedule,
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

def checkDayStudy(user, schedule, join):
    # 현재 접속한 사용자의 일일 공부 검토
    for j in join:
        if schedule.filter(studyGroup=j.studyGroup, studySch=True):
            # 일일 공부 일정 이미 존재
            print("Exist!")
        else:
            # 일일 공부 일정이 없음
            date = datetime.now().date()
            if Study.objects.filter(user=user, studyGroup=j.studyGroup, date=date, finish=True):
                # 1) study 모델에 있음(user=user, studyGroup=studyGroup, date=today, finish=True)
                print("Already Clear!")
            else:
                # 2) 아직 일일 공부 일정이 만들어지지 않음 -> 일일 공부 일정 생성
                print("Not Study!")
                title = "일일 공부"
                time = datetime(1, 1, 1, 23, 59, 59).time()
                content = str(j.studyGroup.title) +" "+ str(date)[5:] + " 일일 공부"
                studyGroup = j.studyGroup
                studySch = True
                Schedule.objects.create(title=title, date=date, time=time, content=content, studyGroup=studyGroup, studySch=studySch, user=user)
