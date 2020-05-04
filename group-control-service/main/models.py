from django.db import models
from django.conf import settings

class Group(models.Model):
    title = models.CharField(max_length=50)
    groupType = models.CharField(max_length=50, default='토익 스터디')
    fee = models.IntegerField(default=100)
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    code = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    start = models.DateField(null=True)
    end = models.DateField(null=True)
    count = models.IntegerField(default=1)

class Join(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, default=0)
    penalty = models.IntegerField(default=0)





