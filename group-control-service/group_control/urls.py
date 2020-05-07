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
    path('book_main', showBookMain, name='book_main'),
    path('book_create', showCreateBook, name='book_create'),
]