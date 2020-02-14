from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request, userId=0):
    # Here the userId contains the id
    # within the url

    # We need to send additional data to confirm that this
    # is the appropriate user and has the authority to 
    # view this page
    
    context = {
        "user": {
            "id": userId
        }
    }
    return render(request, "User/index.html", context)