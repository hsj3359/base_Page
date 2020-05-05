from django.db import models
from django.conf import settings

class StudyGroup(models.Model):
    title = models.CharField(max_length=50)
    groupType = models.CharField(max_length=50, default='토익 스터디')
    start = models.DateField()
    end = models.DateField()
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    code = models.IntegerField()

class Join(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    studyGroup = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, default=0)





