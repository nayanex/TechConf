import logging
from datetime import datetime

import azure.functions as func
import sendgrid
import psycopg2

import orm
import unit_of_work


def main(msg: func.ServiceBusMessage):
    notification_id = int(msg.get_body().decode("utf-8"))
    logging.info(
        "Python ServiceBus queue trigger processed message: %s", notification_id
    )

    # TODO: Get connection to database
    uow: unit_of_work.AbstractUnitOfWork
    orm.start_mappers()

    try:
        # TODO: Get notification message and subject from database using the notification_id
        with uow:
            notification = uow.notifications.get(id=notification_id)
            # TODO: Get attendees email and name
            attendees = uow.attendees.get_all()
            # TODO: Loop through each attendee and send an email with a personalized subject
            for attendee in attendees:
                subject = '{}: {}'.format(attendee.first_name, notification.subject)
                sendgrid.send_email(attendee.email, subject, notification.message)

            # TODO: Update the notification table by setting the completed date and updating the status with the total number of attendees notified
            uow.notifications.update(
                notification_id,
                {
                    "status": "Notified {} attendees".format(len(attendees)),
                    "completed_date": datetime.utcnow(),
                },
            )

    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)


# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python

##################################################
            ## TODO: Refactor This logic into an Azure Function
            ## Code below will be replaced by a message queue
            #################################################
            # attendees = Attendee.query.all()

            # for attendee in attendees:
            #     subject = '{}: {}'.format(attendee.first_name, notification.subject)
            #     send_email(attendee.email, subject, notification.message)

            # notification.completed_date = datetime.utcnow()
            # notification.status = 'Notified {} attendees'.format(len(attendees))
            # db.session.commit()
            # TODO Call servicebus queue_client to enqueue notification ID

            #################################################
            ## END of TODO
            #################################################
