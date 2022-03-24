from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
# Create your models here.

class MyUser(AbstractUser):
    mobileno = models.BigIntegerField(blank=True, null=True)
    objects = UserManager()