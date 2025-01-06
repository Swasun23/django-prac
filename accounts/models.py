from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    role = models.ForeignKey('roster.Role', on_delete=models.SET_NULL, null=True, related_name='users')
    shift = models.ForeignKey('roster.Shift', on_delete=models.SET_NULL, null=True, related_name='users')
    reports_to = models.ForeignKey('self', on_delete=models.SET_NULL, null=True,blank=True, related_name='subordinates')

    def __str__(self):
        return self.username

class Employee_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
