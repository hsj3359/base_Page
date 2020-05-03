from django.urls import path
from .views import *

app_name = 'group'

urlpatterns = [
    path('', showGroup, name='group'),
    path('showQuest/', showQuest, name='showQuest'),    # 삭제 예정
    path('notice/', showNotice, name='notice'),
    path('createSche/', createSche, name='createSche'),
    path('createQuest/', createQuest, name='createQuest'),
    path('createNotice/', createNotice, name='createNotice'),
    path('chat/', showChat, name='chat'),
    path('shareReward/', shareReward, name='shareReward'),
    path('modify/', modify, name='modify'),
    path('invite/', invite, name='invite'),
    path('retire/', retire, name='retire'),

    path('approveSub/', approveSub, name='approveSub'),
    path('approveFinal/', approveFinal, name='approveFinal'),

    path('unjoin/', unjoin, name='unjoin'),
    path('checkSche/', checkSche, name='checkSche'),
    path('submitSub/', submitSub, name='submitSub'),
    path('checkFinal/', checkFinal, name='checkFinal'),
]