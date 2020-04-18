from django.contrib import admin
from .models import *

@admin.register(Quest)
class QuestAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'created_at', 'end', 'join']

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'time', 'content', 'created_at', 'group']

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at','group']