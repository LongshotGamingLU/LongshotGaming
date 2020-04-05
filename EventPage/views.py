from django.shortcuts import render

# Google Calendar imports
import datetime
from google.oauth2 import service_account
import googleapiclient.discovery

SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'google-credentials.json'
CAL_ID = 'lu.longshotgaming@gmail.com'

def lastDayOfMonth(any_day):
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)  # this will never fail
    return next_month - datetime.timedelta(days=next_month.day)

# Imports calendar from lu.longshotgaming@gmail.com for current month
def importCalendar():
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)

    now = datetime.datetime.utcnow().isoformat() + 'Z'
    monthBegin = datetime.datetime.today().replace(day=1)
    monthEnd = lastDayOfMonth(datetime.datetime.today())

    events_result = service.events().list(calendarId=CAL_ID,timeMin=(monthBegin.isoformat() + 'Z'),timeMax=(monthEnd.isoformat() + 'Z')).execute()

    events = events_result.get('items', [])

    # PrettyEvents will contain a list of events that are tuple objects.
    # Each object will be formatted as:
    # (date, summary) where the format of the objects are:
    #    Date:    String Format "YYYY-MM-DD", which is, Year-Month-Day
    #    Summary: String
    prettyEvents = {
        'events': []
    }
    for e in events:
        if (e.get('summary') != None):
            if (e['start'].get('date') != None):
                prettyEvents['events'].append( ([(e['start']['date'])], e['summary']) )
            elif (e['start'].get('dateTime') != None):
                dateString = e['start']['dateTime'][:10]
                try:
                    dateTime = datetime.datetime.strptime(dateString, '%Y-%m-%d')
                    prettyEvents['events'].append( ([dateTime.date().strftime("%Y-%m-%d")], e['summary']) )
                except ValueError as e:
                    print("Unable to parse calendar event: " + e['summary'] + ". Skipping event.")
            else:
                print("Unknown date for event: " + e['summary'] + ". Skipping event.")
        else:
            print("Uknown summary for event. Skipping event.")
    
    return prettyEvents
            

# Create your views here.
def index(request):
    context = {}
    prettyEvents = importCalendar()
    #print(prettyEvents['events'])
    return render(request, "EventPage/index.html", prettyEvents)