from flask import Flask
import requests
import datetime



app = Flask(__name__)

MICROSERVICE_URL = "http://127.0.0.1:8001/process"

#Link below for getting your app password (xxxx xxxx xxxx xxxx)
#https://support.google.com/mail/answer/185833?hl=en

now = datetime.datetime.now()
future = now + datetime.timedelta(seconds=10) # 10 seconds in the future
data = {
    "sender_email": "[YOUR_EMAIL]",
    "receiver_email": "[RECEIVER_EMAIL]",
    "password": "xxxx xxxx xxxx xxxx",
    "message": "[BODY_TEXT]",
    "notification_datetime": future.isoformat() # For testing, it is set to 10 seconds in the future
}

def call_microservice():

    response = requests.post(MICROSERVICE_URL, json=data)
    return response.json()

if __name__ == "__main__":
    print("Server Running")
    results = call_microservice()
    print(results)

