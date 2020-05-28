from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseRedirect
from main.models import StudyGroup, Join
from .models import *
from .forms import *
from django.contrib.auth.models import User

# index.html
def showGroup(request, pk):
    studyGroup = StudyGroup.objects.get(id=pk)
    for s in Schedule.objects.filter(studyGroup=studyGroup):
        if Schedule.checkSche(s):
            s.delete()
            print("기간이 지난 일정입니다.")
    schedule = Schedule.objects.filter(studyGroup=studyGroup)
    rooms = Room.objects.filter(studyGroup=studyGroup)
    notice = Notice.objects.filter(studyGroup=studyGroup)
    form = ScheduleForm()
    room_form = RoomForm()
    dict = {
        'group':studyGroup,
        'schedule':schedule,
        'rooms':rooms,
        'notice':notice,
        'form': form,
        'room_form':room_form,
        'user': request.user,
    }
    return render(request, "group_control/index.html", dict)

# 일정 생성
def createSche(request, pk):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            studyGroup = StudyGroup.objects.get(id=pk)
            Schedule.objects.create(title=new.title, date=new.date, time=new.time, content=new.content, studyGroup=studyGroup, user=request.user)
            print("Success create schedule!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# 일정 수정
def modifySche(request, pk, pk2):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            update = form.save(commit=False)
            sche = Schedule.objects.get(id=pk2)
            sche.title = update.title
            sche.date = update.date
            sche.time = update.time
            sche.content = update.content
            sche.save()
            print("Success modify schedule!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# 일정 삭제
def deleteSche(request, pk, pk2):
    if request.method == 'POST':
        sche = Schedule.objects.get(id=pk2)
        sche.delete()
        print("Success delete schedule!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

#대화방 생성
def createRoom(request, pk):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            studyGroup = StudyGroup.objects.get(id=pk)
            Room.objects.create(title=new.title, studyGroup=studyGroup)
            print("Success create room!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# notice.html
def showNotice(request, pk):
    # user = request.user
    studyGroup = StudyGroup.objects.get(id=pk)
    notice = Notice.objects.filter(studyGroup=studyGroup)
    rooms = Room.objects.filter(studyGroup=studyGroup)
    form = NoticeForm()
    dict = {
        'group': studyGroup,
        'notice': notice,
        'form': form,
        'rooms': rooms,
    }
    return render(request, 'group_control/notice.html', dict)

# 공지 생성
def createNotice(request, pk):
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            studyGroup = StudyGroup.objects.get(id=pk)
            Notice.objects.create(title=new.title, type=new.type, content=new.content, studyGroup=studyGroup)
            print("Success create notice!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def showChat(request, pk, pk2):
    user = request.user
    studyGroup = StudyGroup.objects.get(id=pk)
    join = Join.objects.filter(studyGroup=studyGroup)    # 그룹에 참여한 유저 데이터
    form = ChatForm()
    rooms = Room.objects.filter(studyGroup=studyGroup)
    room = Room.objects.get(id=pk2)
    chat = Chat.objects.filter(studyGroup=studyGroup, room=room)
    if request.method == 'POST':
        author_name = request.POST.get('author', None)
        user = User.objects.get(username=author_name)
        file = request.POST.get('file', None)
        message = request.POST.get('message', None)
        created_at = request.POST.get('created_at', None)
        print("Server receive message: ", author_name, message, created_at)
        Chat.objects.create(author=user, studyGroup=studyGroup, room=room, file=file, message=message)
    dict = {
            'group': studyGroup,
            'room': room,
            'join': join,
            'chat': chat,
            'form': form,
            'rooms': rooms,
            'user': user
        }
    return render(request, 'group_control/chatSample.html', dict)

def showChat(request, pk, pk2):
    user = request.user
    studyGroup = StudyGroup.objects.get(id=pk)        # 그룹 데이터
    room = Room.objects.get(id=pk2)
    join = Join.objects.filter(studyGroup=studyGroup)
    chat = Chat.objects.filter(studyGroup=studyGroup, room=room)
    form = ChatForm()

    dict = {
        'user': user,
        'group': studyGroup,
        'room': room,
        'join': join,
        'chat': chat,
        'form': form,
    }
    return render(request, 'group_control/chatSample.html', dict)

# book.html
def showBookList(request, pk):
    studyGroup = StudyGroup.objects.get(id=pk)
    book = Book.objects.filter(studyGroup=studyGroup)
    rooms = Room.objects.filter(studyGroup=studyGroup)
    dict = {
        'group': studyGroup,
        'book': book,
        'rooms': rooms,
    }
    return render(request, 'group_control/book.html', dict)

# book 내용 보기
def showBookContent(request, pk, pk2):
    studyGroup = StudyGroup.objects.get(id=pk)
    book = Book.objects.get(id=pk2)
    rooms = Room.objects.filter(studyGroup=studyGroup)
    dict = {
        'group': studyGroup,
        'book': book,
        'rooms': rooms,
    }
    return render(request, 'group_control/book_main.html', dict)

def createBook(request, pk):
    user = request.user
    studyGroup = StudyGroup.objects.get(id=pk)
    rooms = Room.objects.filter(studyGroup=studyGroup)
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.author = user
            book.studyGroup = studyGroup
            book.save()
            print("Success create book!")
            return redirect('./book')
    else:
        form = BookForm()
    dict = {
        'group': studyGroup,
        'form': form,
        'rooms': rooms,
    }

    return render(request, 'group_control/book_create.html', dict)


# -----------------------------------------------------------------------------
# import time
# from datetime import datetime, timedelta

# def showGraph(studyGroup):
#     join = Join.objects.filter(studyGroup=studyGroup)
#     date = datetime.now().date()
#     graph_dict = {}
#     v_dict = {}
#     days = 3
#     for i in range(4):
#         prevDate = date - timedelta(days=days)
#         v_dict = {}
#         for j in join:
#             if Study.objects.filter(user=j.user, studyGroup=studyGroup, date=prevDate):
#                 second = Study.objects.get(user=j.user, studyGroup=studyGroup, date=prevDate).total
#                 hour = 0
#                 min = 0
#                 while second > 3600:
#                     second -= 3600
#                     hour += 1
#                 while second > 60:
#                     second -= 60
#                     min += 1
#                 min = int(min/60*100)/100
#                 total = hour + min
#                 v_dict[j.user.username] = str(total)
#             else:
#                 v_dict[j.user.username] = '0'
#         graph_dict[prevDate.strftime('%m.%d')] = v_dict
#         days -= 1
#     print(graph_dict)
#     return graph_dict



