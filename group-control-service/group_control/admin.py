from django.contrib import admin
from .models import *

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'time', 'content', 'created_at']

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']

@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    list_display = ['user', 'studyGroup', 'total', 'play']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['author', 'studyGroup', 'title', 'created_at']