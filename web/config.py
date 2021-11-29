import os

from dotenv import load_dotenv

basedir = os.path.abspath("")
load_dotenv(os.path.join(basedir, ".env"))


class BaseConfig:
    DEBUG = True
    POSTGRES_URL = os.environ.get("POSTGRES_URL")
    POSTGRES_USER = os.environ.get("POSTGRES_USER")
    POSTGRES_PW = os.environ.get("POSTGRES_PW")
    POSTGRES_DB = os.environ.get("POSTGRES_DB")
    DB_URL = "postgresql://{user}:{pw}@{url}/{db}".format(
        user=POSTGRES_USER, pw=POSTGRES_PW, url=POSTGRES_URL, db=POSTGRES_DB
    )
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI") or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = "LWd2tzlprdGHCIPHTd4tp5SBFgDszm"
    SERVICE_BUS_CONNECTION_STRING = os.environ.get("SERVICE_BUS_CONNECTION_STRING")
    SERVICE_BUS_QUEUE_NAME = "notificationqueue"
    ADMIN_EMAIL_ADDRESS = "info@techconf.com"
    SENDGRID_API_KEY = ""  # Configuration not required, required SendGrid Account


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
