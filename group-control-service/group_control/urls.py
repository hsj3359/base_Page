from django.urls import path
from .views import *

app_name = 'group_control'

urlpatterns = [
    path('showGroup/', showGroup, name='showGroup'),
    path('showQuest/', showQuest, name='showQuest'),
    path('showNotice/', showNotice, name='showNotice'),

    path('shareReward/', shareReward, name='shareReward'),


    path('modify/', modify, name='modify'),
    path('invite/', invite, name='invite'),
    path('retire/', retire, name='retire'),
    path('createSche/', createSche, name='createSche'),
    path('createSub/', createSub, name='createSub'),
    path('createNote/', createNote, name='createNote'),
    path('approveSub/', approveSub, name='approveSub'),
    path('approveFinal/', approveFinal, name='approveFinal'),

    path('unjoin/', unjoin, name='unjoin'),
    path('checkSche/', checkSche, name='checkSche'),
    path('submitSub/', submitSub, name='submitSub'),
    path('checkFinal/', checkFinal, name='checkFinal'),
]