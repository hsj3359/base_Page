from django.db import models
from main.models import StudyGroup
from django.conf import settings
from datetime import datetime
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

def file_path(instance, filename):
    from time import strftime
    return '{}/{}/{}'.format(instance.studyGroup.title, strftime('%y-%m-%d'), filename)

class Schedule(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField(null=True)
    content = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    studyGroup = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['created_at']

    # 일정 시간과 현재 시간을 비교하여 지났을 시, 자동으로 그 일정을 삭제
    def checkSche(self):
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

class Book(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    studyGroup = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, default=0)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=9999, null=True)
    subject = models.CharField(max_length=50, default="default")
    created_at = models.DateTimeField(auto_now_add=True)

class Room(models.Model):
    title = models.CharField(max_length=50)
    studyGroup = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, default=0)

class Chat(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    studyGroup = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, default=0)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, default=0)
    photo = ProcessedImageField(upload_to=file_path,
                                processors=[ResizeToFill(100, 100)],
                                format='JPEG',
                                options={'quality': 90},
                                null=True
                                )
    message = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    studyGroup = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, default=0)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=9999, null=True)
    subject = models.CharField(max_length=50)
    photo = ProcessedImageField(upload_to=file_path,
                                processors=[ResizeToFill(100, 100)],
                                format='JPEG',
                                options={'quality': 90},
                                null=True
                                )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
