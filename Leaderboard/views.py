from django.shortcuts import render
# Make sure to import any extra models you will need!
from Leaderboard.models import Rank
from User.models import User 

def saveScore(userId, rank, gamesWon, gamesLost):
    # First get the user that is the foreign key for this rank
    user = User.objects.get(userId=userId)

    # Next, update or create the user
    Rank.objects.update_or_create(userId=user, rank=rank, gamesWon=gamesWon, gamesLost=gamesLost)

def getScore(userId):
    # First try to get the user for the score we want to get
    try:
        user = User.objects.get(userId=userId)
    except model.DoesNotExist:
        user = None

    # If no user exists, just return None
    if user == None:
        return None

    # Create or get user (If user does not exist, default rank and stuff is all 0)
    obj, created = Rank.objects.get_or_create(userId=user, defaults={'rank':0, 'gamesWon':0, 'gamesLost':0})

    # Return appropriate user, if we still didn't manage to get one, 
    # just return None, and print a message
    if obj != None:
        return obj 
    elif created != None:
        return created
    else:
        print("An unreconcilable error has occured... We can no longer create or get objects for whatever reason in Leaderboard.views.py")

    return None

def index(request):
    users = []

    # Create a list of users, with rank and username and everything to pass to the front end
    for user in User.objects.all():
        rank = getScore(user.userId)
        if rank != None:
            userCtx = {"rank": rank.rank, "gamesWon": rank.gamesWon, "gamesLost": rank.gamesLost, "first_name": user.first_name, "last_name": user.last_name}
            users.append(userCtx)


    return render(request, 'Leaderboard/index.html', context={"users":users})