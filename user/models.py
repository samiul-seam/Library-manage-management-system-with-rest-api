from django.db import models
from django.contrib.auth.models import AbstractUser
from user.managers import CustomUserManager

 
# Create your models here.
class User(AbstractUser):
    username = None
    uid = models.CharField(max_length=50, unique=True)
    batch = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    USERNAME_FIELD = "uid"
    REQUIRED_FIELDS =[]

    objects = CustomUserManager()

    def __str__(self):
        return self.uid
    
    