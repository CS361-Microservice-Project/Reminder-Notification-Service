# Reminder-Notification-Service

## Description
Delivers notifications and/or reminders through email.

## Requesting Data
To request, the client-side must send a JSON object over port 8001 sent to a URL path "/process".

Client-Side Example:

```
MICROSERVICE_URL = "http://127.0.0.1:8001/process"
now = datetime.datetime.now()
future = now + datetime.timedelta(seconds=10) # 10 seconds in the future
data = {
    "sender_email": "[YOUR_EMAIL]",
    "receiver_email": "[RECEIVER_EMAIL]",
    "password": "xxxx xxxx xxxx xxxx",
    "message": "[BODY_TEXT]",
    "notification_datetime": future.isoformat() # For testing, it is set to 10 seconds in the future
}

def call_microservice(data):
  response = requests.post(MICROSERVICE_URL, json=data)
```

## Receiving Data
To receive, the server-side will return a json object message to the client. This message may be arbitrary, as different programs may need different information. By default, the server-side will simply return a success message. The client-side reception will be a single line:

`response = requests.post(MICROSERVICE_URL, json=data)`

In this form, the JSON object will have been converted back into a string for the main program to manipulate as necessary.

# UML Diagram

![UML Diagram](UML_Reminder_Notification_Service.png)
