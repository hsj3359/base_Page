from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('', login_check, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('forgot_password/', forgot_password, name='forgot_password'),

]