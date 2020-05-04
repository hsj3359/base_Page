from django.urls import path
from .views import *

app_name = 'group'

urlpatterns = [
    path('', showGroup, name='group'),
    path('notice/', showNotice, name='notice'),
    path('createSche/', createSche, name='createSche'),
    path('createNotice/', createNotice, name='createNotice'),
    path('chat/', showChat, name='chat'),
    path('book/', showBook, name='book'),
]