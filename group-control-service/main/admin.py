from django.contrib import admin
from .models import *

@admin.register(StudyGroup)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'groupType', 'start', 'end']

@admin.register(Join)
class JoinAdmin(admin.ModelAdmin):
    list_display = ['user', 'studyGroup']