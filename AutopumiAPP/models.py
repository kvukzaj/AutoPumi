from django.db import models
#from django.contrib.auth.models import AbstractUser
#from django.db import models

class User(models.Model):
    username = models.CharField(max_length=65)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=65)

    def __str__(self):
        return self.firstname

# Create your models here.

class Contact(models.Model):
    firstname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname