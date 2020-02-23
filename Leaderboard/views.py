from django.shortcuts import render
# Make sure to import any extra models you will need!
from Leaderboard.models import Rank
from User.models import User

def saveScore(userId, rank, gamesWon, gamesLost):
    # First get the user that is the foreign key for this rank
    user = User.objects.get(userId=userId)

    # Now I can use Django's built-in update_or_create function which will update
    # the row at the specified userId if it exists, or create a new row if it does not
    # exist. You can check that it worked afterwards to by going to the admin page.
    Rank.objects.update_or_create(userId=user, rank=rank, gamesWon=gamesWon, gamesLost=gamesLost)

    # When I go to admin page, I can see that the function call successfully saved the user :)

def getScore(userId):
    # First get the user for the score we want to get
    user = User.objects.get(userId=userId)

    # Next simply return the rank, using django's built-in functions and the user (foreign key)
    return Rank.objects.get(userId=user)

    # For more information on how Django's built-in functions for getting stuff works check out:
    # https://docs.djangoproject.com/en/3.0/ref/models/expressions/

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

    # Test our saveScore function and see if it works, I created a fake user
    # with ID of 1 using the admin page
    saveScore(1, 10, 20, 3)

    # Test the getScore function, should return the score that I just saved in the line above
    score = getScore(1)
    print(str(score.userId) + " " + str(score.gamesWon) + " " + str(score.gamesLost) + " " + str(score.rank))

    return render(request, 'Leaderboard/index.html', context)