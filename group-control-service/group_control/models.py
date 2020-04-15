from django.db import models
from main.models import Group, Join

class Quest(models.Model):
    title = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    exp = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    join = models.ForeignKey(Join, on_delete=models.CASCADE, default=0)

class Schedule(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, default=0)

class Notice(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, default=0)