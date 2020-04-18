from django.db import models
from django.conf import settings

class Group(models.Model):
    title = models.CharField(max_length=50)
    finalTarget = models.CharField(max_length=200)
    groupType = models.CharField(max_length=50, default='토익 스터디')
    fee = models.IntegerField(default=100)
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Join(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, default=0)
    role = models.CharField(max_length=50, default='member')
    exp = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    penalty = models.IntegerField(default=0)





