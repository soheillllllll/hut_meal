from django.db import models

# Create your models here.
from django.contrib.auth.models import User




class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=100, default='normal')
    address = models.CharField(max_length=700, default='address')
    phone = models.CharField(max_length=100, default='phone')

    def __str__(self):
        return self.user.username