from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    client_is = models.BooleanField(default=False)
    staff_is = models.BooleanField(default=False)


class Client(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=10)


class Staff(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=10)
