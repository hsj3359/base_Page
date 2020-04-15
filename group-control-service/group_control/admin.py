from django.contrib import admin
from .models import *

@admin.register(Quest)
class QuestAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'created_at', 'start', 'end', 'join']

@admin.register(Schedule)
class QuestAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'created_at', 'group']

@admin.register(Notice)
class QuestAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at','group']