from django.db import models

# Create your models here.
class Rank(models.Model):
    userId = models.ForeignKey(
        'User.User',
        on_delete=models.CASCADE,
    )
    rank = models.IntegerField()
    gamesWon = models.IntegerField()
    gamesLost = models.IntegerField()