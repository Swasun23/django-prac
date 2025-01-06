from django.db import models
from django.utils import timezone

# Create your models here.
class LeaveRequest(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='leave_requests')
    reason = models.TextField()
    date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')
    superior = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True, related_name='leave_requests_to_approve')

    def __str__(self):
        return f"Leave request from {self.user.username} ({self.status})"
