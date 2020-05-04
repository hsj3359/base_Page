from django.db import models
from main.models import StudyGroup

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