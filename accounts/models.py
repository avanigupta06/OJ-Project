from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserExtension(models.Model):
    USER_TYPES = (
        ('normal', 'Normal User'),
        ('setter', 'Problem Setter'),
        ('admin', 'Admin'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='normal')

    def __str__(self):
        return f"{self.user.username} ({self.user_type})"