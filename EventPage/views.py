from django.shortcuts import render

# Google Calendar imports
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
# SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

# def importCalendar():
#     creds = None

#     if os.path.exists('token.pickle'):
#         with open('token.pickle', 'rb') as token:
#             creds = pickle.load(token)
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             f = open('credentials.json', 'w')
#             f.write(os.environ.get('GOOGLE_CRED_FILE'))
#             f.close()
#             flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
#             creds = flow.run_local_server(port=0)
#         with open('token.pickle', 'wb') as token:
#             pickle.dump(creds, token)
#     service = build('calendar', 'v3', credentials=creds)

#     now = datetime.datetime.utcnow().isoformat() + 'Z'
#     print("Getting the upcoming 10 events")
#     events_result = service.events().list(calendarId='primary', timeMin=now, maxResults=10, singleEvents=True, orderBy='startTime').execute()
#     events = events_result.get('items', [])
    
#     if not events:
#         print("No upcoming events found.")
#     else:
#         start = event['start'].get('dateTime', event['start'].get('date'))
#         print(start, event['summary'])

# Create your views here.
def index(request):
    context = {}
    importCalendar()
    return render(request, "EventPage/index.html", context)