from django.shortcuts import render
from main.models import *
from .models import *

def showGroup(request, pk):
    # 그룹에 관한 데이터를 보여주는 기능
    # 일정을 달력과 리스트의 형태로 표시
    # 개인의 능력치를 수치나 그래프로 표시
    # 각 멤버의 성과를 그래프로 표시
    # 공지 표시
    # 과제 표시
    currGroup = Group.objects.get(id=pk)
    currJoin = Join.objects.get(group=currGroup, user=request.user)
    schedule = Schedule.objects.filter(group=currGroup)
    notice = Notice.objects.filter(group=currGroup)
    quest = Quest.objects.filter(join=currJoin)
    questCount = 0
    for q in quest:
        questCount += 1
    dict = {
        'group':currGroup,
        'join':currJoin,
        'schedule':schedule,
        'notice':notice,
        'quest': quest,
        'questCount': questCount,
    }
    return render(request, "group_control/index.html", dict)

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
def createSche(request):
    # 일정 생성 기능
    # 호스트 기능
    return

def createSub(request):
    # 과제 생성 기능
    # 호스트 기능
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



