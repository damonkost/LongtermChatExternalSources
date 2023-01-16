import requests
import json
# enter your API credentials
client_id = "170651117664-r266gkgtaaeosih4apesreedhef1fchq.apps.googleusercontent.com"
client_secret = "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"
# use the OAuth2 protocol to authorization
oauth2_url = 'https://accounts.google.com/o/oauth2/token'
payload = {
 'client_id': client_id,
 'client_secret': client_secret,
 'grant_type': 'authorization_code'
}
response = requests.post(oauth2_url, data=payload)
token = response.json()["AIzaSyAbeFATj8XekaSWLaM0o-EmrCrFyfR_wiM"]
# create a connection to the Google Calendar API
api_url='https://www.googleapis.com/calendar/v3'
headers = { 'Authorization': 'Bearer {}'.format(token) }
# retrieve the calendar events
events_url = api_url + '/calendars/primary/events'
events_response = requests.get(events_url, headers=headers)
events_data = events_response.json()
events = events_data['items']
# write calendar events to a text file
with open('calendar-events.txt', 'w') as f:
 for event in events:
  line = '{}: {}\n'.format(event['start']['dateTime'],event['summary'])
 f.write(line)