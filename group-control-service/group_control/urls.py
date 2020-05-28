from django.urls import path
from .views import *

app_name = 'group'

urlpatterns = [
    path('', showGroup, name='group'),
    path('createSche/', createSche, name='createSche'),
    path('modifySche/<int:pk2>', modifySche, name='modifySche'),
    path('deleteSche/<int:pk2>', deleteSche, name='deleteSche'),
    path('notice/', showNotice, name='notice'),
    path('notice/create/', createNotice, name='createNotice'),
    path('createRoom/', createRoom, name='createRoom'),
    path('chat/<int:pk2>', showChat, name='chat'),
    path('book/', showBookList, name='book'),
    path('book/content/<int:pk2>', showBookContent, name='book_main'),
    path('book/create/', createBook, name='book_create'),

]