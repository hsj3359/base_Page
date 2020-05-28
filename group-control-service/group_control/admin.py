from django.contrib import admin
from .models import *

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'time', 'content', 'created_at']

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['author', 'studyGroup', 'title', 'created_at']

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'studyGroup']

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ['author', 'studyGroup', 'message', 'created_at']