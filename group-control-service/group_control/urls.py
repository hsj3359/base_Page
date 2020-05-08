from django.urls import path
from .views import *

app_name = 'group'

urlpatterns = [
    path('', showGroup, name='group'),
    path('notice/', showNotice, name='notice'),
    path('createSche/', createSche, name='createSche'),
    path('modifySche/<int:pk2>', modifySche, name='modifySche'),
    path('deleteSche/<int:pk2>', deleteSche, name='deleteSche'),
    path('createNotice/', createNotice, name='createNotice'),
    path('chat/', showChat, name='chat'),
    path('book/', showBook, name='book'),
    path('book_main', showBookMain, name='book_main'),
    path('book_create', showCreateBook, name='book_create'),
    path('list', showList, name='list'),
]