# roster/models.py
from django.db import models
from django.utils import timezone

class Role(models.Model):
    name = models.CharField(max_length=50)
    access_level = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Shift(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    days_of_week = models.JSONField(default=list)

    def __str__(self):
        return f"{self.name} ({self.start_time} - {self.end_time})"
    

class Holiday(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField(blank=True)
    
    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.name} on {self.date}"



