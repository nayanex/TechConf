import os

from azure.servicebus import QueueClient
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")

app.secret_key = app.config.get("SECRET_KEY")

#'Endpoint=Endpoint=sb://tech-conf.servicebus.windows.net/'
#'notificationqueue'
queue_client = QueueClient.from_connection_string(
    app.config.get("SERVICE_BUS_CONNECTION_STRING"),
    app.config.get("SERVICE_BUS_QUEUE_NAME"),
)

db = SQLAlchemy(app)

from . import routes
