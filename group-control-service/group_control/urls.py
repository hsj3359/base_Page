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
]