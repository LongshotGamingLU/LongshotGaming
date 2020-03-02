from django.db import models

# Create your models here.
class User(models.Model):
    userId = models.IntegerField(
        primary_key = True
    )
    email = models.CharField(max_length=64, unique=True, blank=False, default="")
    username = models.CharField(max_length=64, unique=True, blank=False, default="")
    first_name = models.CharField(max_length=64, blank=False, default="")
    last_name = models.CharField(max_length=64, blank=False, default="")
    picture = models.CharField(max_length=512, blank=False, default="static/img/users/default.png")
