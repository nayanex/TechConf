import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


def get_postgres_uri():
    host = os.environ.get("POSTGRES_HOST", "localhost")
    port = os.environ.get("POSTGRES_PORT")
    password = os.environ.get("POSTGRES_PW")
    db_name = os.environ.get("POSTGRES_DB")
    user = os.environ.get("POSTGRES_USER")
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"


class Config(object):
    FROM_EMAIL = os.environ.get("FROM_EMAIL")
    SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
