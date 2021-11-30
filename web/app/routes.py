import logging
import requests
import config
from datetime import datetime

from azure.servicebus import ServiceBusMessage
from flask import redirect, render_template, request, session

from app import app, db, servicebus_client
from app.models import Attendee, Conference, Notification


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/Registration", methods=["POST", "GET"])
def registration():
    if request.method == "POST":
        attendee = Attendee()
        attendee.first_name = request.form["first_name"]
        attendee.last_name = request.form["last_name"]
        attendee.email = request.form["email"]
        attendee.job_position = request.form["job_position"]
        attendee.company = request.form["company"]
        attendee.city = request.form["city"]
        attendee.state = request.form["state"]
        attendee.interests = request.form["interest"]
        attendee.comments = request.form["message"]
        attendee.conference_id = app.config.get("CONFERENCE_ID")

        try:
            db.session.add(attendee)
            db.session.commit()
            session["message"] = "Thank you, {} {}, for registering!".format(
                attendee.first_name, attendee.last_name
            )
            return redirect("/Registration")
        except:
            logging.error("Error occurred while saving your information")

    else:
        if "message" in session:
            message = session["message"]
            session.pop("message", None)
            return render_template("registration.html", message=message)
        else:
            return render_template("registration.html")


@app.route("/Attendees")
def attendees():
    attendees = Attendee.query.order_by(Attendee.submitted_date).all()
    return render_template("attendees.html", attendees=attendees)


@app.route("/Notifications")
def notifications():
    notifications = Notification.query.order_by(Notification.id).all()
    return render_template("notifications.html", notifications=notifications)


@app.route("/Notification", methods=["POST", "GET"])
def notification():
    if request.method == "POST":
        notification = Notification()
        # json_data = request.get_json(force=True)
        # value = json_data["myparamname"]
        notification.message = request.form["message"]
        notification.subject = request.form["subject"]
        notification.status = "Notifications submitted"
        notification.submitted_date = datetime.utcnow()

        try:
            db.session.add(notification)
            db.session.commit()

            ##################################################
            ## TODO: Refactor This logic into an Azure Function
            ## Code below will be replaced by a message queue
            #################################################
            # TODO Call servicebus queue_client to enqueue notification ID

            with servicebus_client:
                sender = servicebus_client.get_queue_sender(
                    queue_name=app.config.get("SERVICE_BUS_QUEUE_NAME")
                )
                with sender:
                    send_single_message(sender, notification.id)

            print("Done sending messages")
            print("-----------------------")

            #################################################
            ## END of TODO
            #################################################

            return redirect("/Notifications")
        except:
            logging.error("log unable to save notification")

    else:
        return render_template("notification.html")


def send_single_message(sender, msg):
    # create a Service Bus message
    message = ServiceBusMessage(str(msg))
    # send the message to the queue
    sender.send_messages(message)
    print("Sent a single message")
