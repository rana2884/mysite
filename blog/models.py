from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    message = models.TextField()

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    mobile = models.CharField(max_length=12, default='null')
    email = models.CharField(max_length=120, default='null')
    address = models.TextField(default='null')

    def __str__(self):
        return self.user.username


