from django.db import models

# Create your models here.
class User(models.Model):
    userId = models.IntegerField(
        primary_key = True
    )