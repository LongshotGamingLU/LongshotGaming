from Leaderboard.models import Rank
from django.contrib import admin

# Register your models here.
class RankAdmin(admin.ModelAdmin):
    list_display = ['userId', 'rank', 'gamesWon', 'gamesLost']

admin.site.register(Rank, RankAdmin)