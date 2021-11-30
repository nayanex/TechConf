import logging
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from config import Config


def send_email(to_email, subject, msg):
    message = Mail(
        from_email=Config.FROM_EMAIL,
        to_emails=to_email,
        subject=subject,
        html_content="<strong>{msg}</strong>".format(msg=msg),
    )

    try:
        sg = SendGridAPIClient(Config.SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        return "Message successfully sent."
    except Exception as e:
        print(e.message)
        logging.error(e.message)


# def send_email(email, subject, body):
#     if not app.config.get('SENDGRID_API_KEY'):
#         message = Mail(
#             from_email=app.config.get('ADMIN_EMAIL_ADDRESS'),
#             to_emails=email,
#             subject=subject,
#             plain_text_content=body)

#         sg = SendGridAPIClient(app.config.get('SENDGRID_API_KEY'))
#         sg.send(message)
