

from flask import Flask, jsonify, request
import smtplib
import datetime
import time

# Tutorial - https://www.youtube.com/watch?v=ueqZ7RL8zxM

"""
This is the server side, the microservice. It will listen on port 8001 waiting until
a program POSTS information to it. This information must be in the form of:
data = {
    "sender_email": "senderemail@email.com",
    "receiver_email": "receiveremail@email.com",
    "password": "xxxx xxxx xxxx xxxx",
    "message": "Your message here!",
    "notification_datetime": time.isoformat()
}

notification_datetime must be handled on client side (major program side).

Example:
    time = datetime.datetime.now()

This creates a datetime object in the form of (year, month, hours, minutes, seconds, microseconds)
It must be converted to isoformat (a string) before sending through HTTPS.

Example:
    time = datetime.datetime.now()
    time = time.isoformat()
     
Once sent through to server, it can be reconverted back to a datetime object via fromisoformat()

Example:
    #Create datetime object
    time = datetime.datetime.now()
    
    #Convert to string for jsonification.
    time = time.isoformat()
    
    #Convert from string back to datetime object
    time = datetime.datetime.fromisoformat(time)
    
    
"""

app = Flask(__name__)

@app.route("/process", methods=["POST"])
def generate():

    # Listening on port, waiting to receive json object.
    data = request.get_json()


    # Debugging print statement (optional)
    print("data received")
    for key, value in data.items():
        print(key, value)


    email = data["sender_email"]
    receiver_email = data["receiver_email"]
    app_password = data["password"]
    subject = "Notification!" # Change this if you wish, can also be incorporated on client side.
    message = data["message"]

    # When sending over HTTP, datetime must be converted into isoformat(), here it is converted back to datetime.
    notification_datetime = data["notification_datetime"]
    notification_datetime = datetime.datetime.fromisoformat(notification_datetime)


    # Creates email to be sent.
    text = f"Subject: {subject}\n\n{message}"

    # smtplib starts server and logs into your sender email via app password.
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, app_password)

    # While loop will cross-reference current time with set notification time every second, if so, send email.
    i = 0
    while datetime.datetime.now() < notification_datetime:
        time.sleep(1)
        i += 1
        print(f"{i} seconds have passed...")

    # Debug statement to show it correctly sends email at specified time.
    print(datetime.datetime.now())

    # Sends email.
    server.sendmail(email, receiver_email, text)

    print("Email sent successfully")
    return jsonify("Success, server processing completed.")

if __name__ == "__main__":
    app.run(port=8001)








































