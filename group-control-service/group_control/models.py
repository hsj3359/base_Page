from django.db import models
from main.models import StudyGroup
from django.conf import settings

def file_path(instance, filename):
    return '{}/{}/{}'.format(instance.studyGroup.title, instance.author.username, filename)

class Schedule(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField(null=True)
    content = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    studyGroup = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, default=0)

    class Meta:
        ordering = ['created_at']

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