from django.contrib import admin
from .models import Group, Join

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'groupType', 'start', 'end']

@admin.register(Join)
class JoinAdmin(admin.ModelAdmin):
    list_display = ['user', 'group']