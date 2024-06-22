from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    rating = models.IntegerField(default=0)
    university = models.CharField(max_length=30,default="")
    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)  # Add the rating field here
    university = models.CharField(max_length=30,default="")
    def __str__(self):
        return self.user.username
