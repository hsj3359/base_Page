from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from main.models import StudyGroup, Join
from .models import *
from .forms import *
import time
from datetime import datetime, timedelta
import json

'''
오늘 할 것
그래프 관련 데이터를 json파일에 저장
js가 저장한 json파일을 읽어 그래프 그리게 하기

내일 할 것
대화방

수요일에 할 것
포털웹 과제

다음 주에 할 것
버그 수정
'''
def getStudy(user, studyGroup):
    study = Study.objects.filter(user=user, studyGroup=studyGroup)
    if len(study) == 0:
        study = None
    return study

def showGroup(request, pk):
    user = request.user
    studyGroup = StudyGroup.objects.get(id=pk)
    join = Join.objects.filter(studyGroup=studyGroup)
    userJoin = join.get(user=user)
    schedule = Schedule.objects.filter(studyGroup=studyGroup)
    for s in schedule:
        if s.checkSche():
            if s.studySch:
                userJoin.personal_penalty += 500
                userJoin.save()
            s.delete()
    schedule = Schedule.objects.filter(studyGroup=studyGroup, studySch=False)
    user = request.user
    notice = Notice.objects.filter(studyGroup=studyGroup)
    scheForm = ScheduleForm()
    study = getStudy(user, studyGroup)
    totalPenalty = 0
    for j in join:
        totalPenalty += j.personal_penalty
    graph = showGraph(studyGroup)
    for k, v in graph.items():
        print(k, v)
    dict = {
        'group':studyGroup,
        'join':join,
        'schedule':schedule,
        'notice':notice,
        'sche_form': scheForm,
        'user': user,
        'study':study,
        'totalPenalty':totalPenalty,
        'graph':graph,
    }
    return render(request, "group_control/index.html", dict)

def showNotice(request, pk):
    user = request.user
    studyGroup = StudyGroup.objects.get(id=pk)
    notice = Notice.objects.filter(studyGroup=studyGroup)
    form = NoticeForm()
    study = getStudy(user, studyGroup)
    dict = {
        'group': studyGroup,
        'notice': notice,
        'form': form,
        'study': study,
    }
    return render(request, 'group_control/notice.html', dict)

def createSche(request, pk):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            new_sche = form.save(commit=False)
            studyGroup = StudyGroup.objects.get(id=pk)
            Schedule.objects.create(title=new_sche.title, date=new_sche.date, time=new_sche.time, content=new_sche.content, studyGroup=studyGroup, user=request.user)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def modifySche(request, pk, pk2):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            change_sche = form.save(commit=False)
            sche = Schedule.objects.get(id=pk2)
            sche.title = change_sche.title
            sche.date = change_sche.date
            sche.time = change_sche.time
            sche.content = change_sche.content
            sche.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def deleteSche(request, pk, pk2):
    if request.method == 'POST':
        sche = Schedule.objects.get(id=pk2)
        sche.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def createNotice(request, pk):
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            newNot = form.save(commit=False)
            studyGroup = StudyGroup.objects.get(id=pk)
            Notice.objects.create(title=newNot.title, type=newNot.type, content=newNot.content, studyGroup=studyGroup)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def showChat(request, pk):
    user = request.user
    studyGroup = StudyGroup.objects.get(id=pk)        # 그룹 데이터
    join = Join.objects.filter(studyGroup=studyGroup)    # 그룹에 참여한 유저 데이터
    study = getStudy(user, studyGroup)
    dict = {
        'group': studyGroup,
        'join': join,
        'study': study
    }
    return render(request, 'group_control/chat.html', dict)

def showBook(request, pk):
    user = request.user
    studyGroup = StudyGroup.objects.get(id=pk)
    study = getStudy(user, studyGroup)
    book = Book.objects.filter(studyGroup=studyGroup)
    dict = {
        'group': studyGroup,
        'study': study,
        'book': book,
    }
    return render(request, 'group_control/book.html', dict)

def showBookMain(request, pk, pk2):
    user = request.user
    studyGroup = StudyGroup.objects.get(id=pk)
    study = getStudy(user, studyGroup)
    book = Book.objects.get(id=pk2)
    dict = {
        'group': studyGroup,
        'study': study,
        'book': book,
    }
    return render(request, 'group_control/book_main.html', dict)

def createBook(request, pk):
    user = request.user
    studyGroup = StudyGroup.objects.get(id=pk)
    study = getStudy(user, studyGroup)
    if request.method == 'POST':
        print("try write!")
        form = BookForm(request.POST)
        if form.is_valid():
            print("book is valid!")
            book = form.save(commit=False)
            book.author = user
            book.studyGroup = studyGroup
            book.save()
            print("write book!")
            return redirect('./book')
    else:
        form = BookForm()

    dict = {
        'group': studyGroup,
        'study': study,
        'form': form,
    }

    return render(request, 'group_control/book_create.html', dict)

def showPost(request, pk):
    user = request.user
    studyGroup = StudyGroup.objects.get(id=pk)
    post = Post.objects.filter(studyGroup=studyGroup)
    form = PostForm()
    study = getStudy(user, studyGroup)
    dict = {
        'group': studyGroup,
        'post': post,
        'form': form,
        'study':study
    }
    return render(request, 'group_control/post.html', dict)

def createPost(request, pk):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.studyGroup = StudyGroup.objects.get(id=pk)
            post.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def startStudy(request, pk):
    if request.method == 'POST':
        user = request.user
        studyGroup = StudyGroup.objects.get(id=pk)
        Study.objects.create(user=user, studyGroup=studyGroup, play=True)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def endStudy(request, pk):
    # 공부 중(play=True)이라면 end에 현재 시간, total필드에 총 공부 시간(end - start), 공부끝(play=False)
    # total이 일정 시간보다 큰 경우, 일정 완료(finish=True)
    if request.method == 'POST':
        user = request.user
        studyGroup = StudyGroup.objects.get(id=pk)
        study = Study.objects.get(user=user, studyGroup=studyGroup, play=True)
        study.end = datetime.now().time()
        start = (study.start.hour * 60 + study.start.minute) * 60 + study.start.second
        end = (study.end.hour * 60 + study.end.minute) * 60 + study.end.second
        study.total = end-start
        study.play = False
        if study.total > 60:
            study.finish = True
            Schedule.objects.get(user=user, date=study.date, studyGroup=studyGroup, studySch=True).delete()
            study.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def showGraph(studyGroup):
    join = Join.objects.filter(studyGroup=studyGroup)
    date = datetime.now().date()
    graph_dict = {}
    v_dict = {}
    days = 3
    for i in range(4):
        prevDate = date - timedelta(days=days)
        v_dict = {}
        for j in join:
            if Study.objects.filter(user=j.user, studyGroup=studyGroup, date=prevDate):
                second = Study.objects.get(user=j.user, studyGroup=studyGroup, date=prevDate).total
                hour = 0
                min = 0
                while second > 3600:
                    second -= 3600
                    hour += 1
                while second > 60:
                    second -= 60
                    min += 1
                min = int(min/60*100)/100
                total = hour + min
                v_dict[j.user.username] = str(total)
            else:
                v_dict[j.user.username] = '0'
        graph_dict[prevDate.strftime('%m.%d')] = v_dict
        days -= 1
    print(graph_dict)
    return graph_dict



