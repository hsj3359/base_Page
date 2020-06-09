from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseRedirect
from main.models import StudyGroup, Join
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages

# group_control의 모든 템플릿이 사용하는 공통 데이터를 딕셔너리에 저장
def base(pk):
    studyGroup = StudyGroup.objects.get(id=pk)
    join = Join.objects.filter(studyGroup=studyGroup)
    rooms = Room.objects.filter(studyGroup=studyGroup)
    room_form = RoomForm()
    dict = {
        'group': studyGroup,
        'join': join,
        'rooms': rooms,
        'room_form': room_form,
    }
    return dict

# index.html
def showGroup(request, pk):
    base_dict = base(pk)
    studyGroup = base_dict['group']
    for s in Schedule.objects.filter(studyGroup=studyGroup):
        if Schedule.checkSche(s):
            s.delete()
            print("기간이 지난 일정입니다.")
    schedule = Schedule.objects.filter(studyGroup=studyGroup)
    notice = Notice.objects.filter(studyGroup=studyGroup)
    form = ScheduleForm()
    dict = {
        'schedule':schedule,
        'notice':notice,
        'form': form,
        'user': request.user,
    }
    dict.update(base_dict)
    return render(request, "group_control/index.html", dict)

# 일정 생성
def createSche(request, pk):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            studyGroup = StudyGroup.objects.get(id=pk)
            Schedule.objects.create(title=new.title, date=new.date, time=new.time, content=new.content, studyGroup=studyGroup, user=request.user)
            messages.info(request, "일정을 생성하였습니다.")
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
            messages.info(request, "일정을 수정하였습니다.")
            print("Success modify schedule!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# 일정 삭제
def deleteSche(request, pk, pk2):
    if request.method == 'POST':
        sche = Schedule.objects.get(id=pk2)
        sche.delete()
        print("Success delete schedule!")
        messages.info(request, "일정을 삭제하였습니다.")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

#대화방 생성
def createRoom(request, pk):
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            studyGroup = StudyGroup.objects.get(id=pk)
            Room.objects.create(title=new.title, studyGroup=studyGroup)
            messages.info(request, "대화방을 생성하였습니다.")
            print("Success create room!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# notice.html
def showNotice(request, pk):
    base_dict = base(pk)
    studyGroup = base_dict['group']
    notice = Notice.objects.filter(studyGroup=studyGroup)
    form = NoticeForm()
    dict = {
        'notice': notice,
        'form': form,
    }
    dict.update(base_dict)
    return render(request, 'group_control/notice.html', dict)

# 공지 생성
def createNotice(request, pk):
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            studyGroup = StudyGroup.objects.get(id=pk)
            Notice.objects.create(title=new.title, type=new.type, content=new.content, studyGroup=studyGroup)
            messages.info(request, "공지를 생성하였습니다.")
            print("Success create notice!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def showChat(request, pk, pk2):
    user = request.user
    studyGroup = StudyGroup.objects.get(id=pk)
    join = Join.objects.filter(studyGroup=studyGroup)    # 그룹에 참여한 유저 데이터
    rooms = Room.objects.filter(studyGroup=studyGroup)
    room = Room.objects.get(id=pk2)
    chat = Chat.objects.filter(studyGroup=studyGroup, room=room)
    if request.method == 'POST':
        author_name = request.POST.get('author', None)
        user = User.objects.get(username=author_name)
        message = request.POST.get('message', None)
        photo = request.POST.get('photo', None)
        created_at = request.POST.get('created_at', None)
        print("Server receive message: ", author_name, message, created_at)
        Chat.objects.create(author=user, studyGroup=studyGroup, room=room, photo=photo, message=message)
    dict = {
            'group': studyGroup,
            'room': room,
            'join': join,
            'chat': chat,
            'rooms': rooms,
            'user': user
        }
    return render(request, 'group_control/chatSample.html', dict)

#대화방 파일 업로드
def uploadImage(request, pk, pk2):
    if request.method == 'POST':
        studyGroup = StudyGroup.objects.get(id=pk)
        room = Room.objects.get(id=pk2)
        user = request.user;
        photo = request.POST.get('photo')
        message = photo
        print("Server receive file: ", photo)
        Chat.objects.create(author=user, studyGroup=studyGroup, room=room, photo=photo, message=message)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# book.html
def showBookList(request, pk):
    base_dict = base(pk)
    studyGroup = base_dict['group']
    book = Book.objects.filter(studyGroup=studyGroup)
    subject_set = set()
    for b in book:
        subject_set.add(b.subject)
    book_dict = {}
    for s in subject_set:
        li = []
        for b in book:
            if s == b.subject:
                li.append(b)
        book_dict[s] = li
    dict = {
        'book': book,
        'book_dict': book_dict
    }
    dict.update(base_dict)
    return render(request, 'group_control/book.html', dict)

# book 내용 보기
def showBookContent(request, pk, pk2):
    base_dict = base(pk)
    book = Book.objects.get(id=pk2)
    dict = {
        'book': book,
    }
    dict.update(base_dict)
    return render(request, 'group_control/book_main.html', dict)

def createBook(request, pk):
    user = request.user
    base_dict = base(pk)
    studyGroup = base_dict['group']
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.author = user
            book.studyGroup = studyGroup
            book.save()
            messages.info(request, "학습노트를 생성하였습니다.")
            print("Success create book!")
            return redirect('/group/{}/book'.format(pk))
    else:
        form = BookForm()
    dict = {
        'form': form,
    }
    dict.update(base_dict)
    return render(request, 'group_control/book_create.html', dict)

def showVideo(request, pk):
    base_dict = base(pk)
    dict = {
    }
    dict.update(base_dict)
    return render(request, 'group_control/videoSample.html', dict)

def showPost(request, pk):
    base_dict = base(pk)
    studyGroup = base_dict['group']
    post = Post.objects.filter(studyGroup=studyGroup)
    subject_set = set()
    for p in post:
        subject_set.add(p.subject)
    post_dict = {}
    for s in subject_set:
        li = []
        for p in post:
            if s==p.subject:
                li.append(p)
        post_dict[s] = li
    dict = {
        'post_dict': post_dict,
    }
    dict.update(base_dict)
    return render(request, 'group_control/post.html', dict)

def createPost(request, pk):
    base_dict = base(pk)
    studyGroup = base_dict['group']
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.studyGroup = studyGroup
            post.save()
            messages.info(request, "자료를 업로드하였습니다.")
            return redirect('/group/{}/post'.format(pk))
    else:
        form = PostForm()
        dict = {
            'form': form,
        }
        dict.update(base_dict)
    return render(request, 'group_control/post_create.html', dict)

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



