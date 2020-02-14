from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "Gabe": {
            "Wins": 20,
            "Losses": 2,
            "Rank": 12
        },
        "Robert": {
            "Wins": 12,
            "Losses": 2,
            "Rank": 10
        }
    }

    return render(request, 'Leaderboard/index.html', context)