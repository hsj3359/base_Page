from django.db import models
from main.models import StudyGroup
from django.conf import settings
from datetime import datetime, timedelta
from django.shortcuts import redirect

def file_path(instance, filename):
    return '{}/{}/{}'.format(instance.studyGroup.title, instance.author.username, filename)

class Schedule(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField(null=True)
    content = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    studyGroup = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, default=0)
    studySch = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['created_at']

    def checkSche(self):
        # 일정 시간과 현재 시간을 비교하여 지났을 시, 자동으로 그 일정을 삭제
        schDate = str(self.date)
        schTime = str(self.time)
        schYear = int(schDate[:4])
        schMon = int(schDate[5:7])
        schDay = int(schDate[8:10])
        schHour = int(schTime[:2])
        schMin = int(schTime[3:5])
        schSec = int(schTime[6:8])
        sch = datetime(schYear, schMon, schDay, schHour, schMin, schSec)
        now = datetime.now()
        return sch < now


class Notice(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    studyGroup = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, default=0)
    type = models.CharField(max_length=50, null=True)
    content = models.CharField(max_length=200, null=True)

    class Meta:
        ordering = ['created_at']

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200, null=True)
    file = models.FileField(upload_to=file_path, blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    studyGroup = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

class Study(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    studyGroup = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, default=0)
    date = models.DateField(auto_now_add=True)
    start = models.TimeField(auto_now_add=True)
    end = models.TimeField(null=True)
    total = models.IntegerField(null=True)
    play = models.BooleanField(default=False)
    finish = models.BooleanField(default=False)

class Book(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    studyGroup = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, default=0)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=9999, null=True)
    created_at = models.DateTimeField(auto_now_add=True)