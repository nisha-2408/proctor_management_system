from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager
# Create your models here.


class User(AbstractUser):
    username=None
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255,primary_key = True)
    #usn = models.CharField(max_length = 10)
    is_email_verified = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]
    objects=CustomUserManager()
    def __str__(self):
        return self.email
