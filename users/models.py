from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'), ('Female', 'Female')))
    description = models.TextField(blank=True, null=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    image = models.ImageField(upload_to='media/user', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.full_name

class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    quality = models.CharField(max_length=10, choices=(('Good', 'Good'), ('Bad', 'Bad')))
    image = models.ImageField(upload_to='media/user', null=True, blank=True)


    def __str__(self):
        return f"{self.name}, price: {self.price}"