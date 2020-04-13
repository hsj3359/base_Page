from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('index/', index, name='index'),
    path('createGroup/', createGroup, name='createGroup'),
    path('joinGroup/', joinGroup, name='joinGroup'),
]