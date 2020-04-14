from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from django.shortcuts import render, redirect
from User.models import User
from Leaderboard.views import getScore

# Use Django's built in functions to save/update a user with the following fields, userID is not necessary
def saveOrUpdateUser(email, username, first_name, last_name, picture, userId=-1):
    user = getUser(email=email)
    if user == None:
        if (User.objects.count() == 0):
            userId = User.objects.count()
        else:
            userId = User.objects.order_by("-userId")[0].userId + 1
    else:
        userId = user.userId

    User.objects.update_or_create(userId=userId, email=email, username=username, first_name=first_name, last_name=last_name, picture=picture)

# Get the appropriate user, via userID or email
def getUser(userId=None, email=None):
    if userId != None:
        return User.objects.get(userId=userId)
    elif email != None:
        users = User.objects.filter(email=email)
        if len(users) > 1:
            # Should never get multiple users with same email, if we do, something has gone wrong...
            print("Problem...")
        elif len(users) == 1:
            # Return the user with the email
            return users[0]

    # No user was found, just return None
    return None


def index(request):
    # Check if a user is logged in, then let the HTML/CSS generate accordingly
    user = request.session.get('user')
    if user != None:
        rank = getScore(user['userId'])
        user['rank'] = rank.rank

    return render(request, "User/index.html", {"user": user})

def logout(request):
    # Just reset session data, and then redirect to user page
    request.session['user'] = None
    return redirect('usersIndex')

def create_user(request, response, user, strategy, details, **kwargs):
    # First save/update the user, to make sure that the user is in the local DB
    saveOrUpdateUser(email=details['email'], username=details['username'], first_name=details['first_name'], last_name=details['last_name'], picture=response['picture'])
    
    # Now that the user is saved to the database (or updated), we can attach a cookie to the local session
    # with information about our user
    user = getUser(email=details['email'])
    rank = getScore(user.userId)
    request.session['user'] = {
        'email': user.email,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'picture': user.picture,
        'rank': rank.rank,
        'userId': user.userId
    }

    # Uncomment these print statements to see pipeline details
    # print("Custom pipeline step.")
    # print("Details:")
    # print(details)
    # print("Response:")
    # print(response)

