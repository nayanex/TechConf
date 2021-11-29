import logging
import os
from datetime import datetime

import azure.functions as func
import psycopg2
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

import orm
import unit_of_work


def main(msg: func.ServiceBusMessage):
    notification_id = int(msg.get_body().decode('utf-8'))
    logging.info('Python ServiceBus queue trigger processed message: %s',notification_id)

    # TODO: Get connection to database
    uow: unit_of_work.AbstractUnitOfWork
    orm.start_mappers()

    try:
        # TODO: Get notification message and subject from database using the notification_id
        with uow:
            notification = uow.notifications.get(id=notification_id)
        # TODO: Get attendees email and name
        

        # TODO: Loop through each attendee and send an email with a personalized subject

        # TODO: Update the notification table by setting the completed date and updating the status with the total number of attendees notified

    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
    finally:
        # TODO: Close connection