import logging

import model
from sqlalchemy import (
    Boolean,
    Column,
    Date,
    Float,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
)
from sqlalchemy.dialects.postgresql import BIT, DOUBLE_PRECISION
from sqlalchemy.orm import registry

logger = logging.getLogger(__name__)

metadata = MetaData()
mapper_registry = registry()


notifications = Table(
    "notifications",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("status", String(31), nullable=False),
    Column("message", String(255), nullable=False),
    Column("submitted_date", Date, nullable=True),
    Column("completed_date", Date, nullable=True),
    Column("subject", Date, nullable=False),
)

attendees = Table(
    "attendees",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("first_name", String(255), nullable=False),
    Column("last_name", String(255), nullable=False),
    Column("conference_id", ForeignKey("conference.id"), nullable=False),
    Column("job_position", String(255), nullable=False),
    Column("email", String(63), nullable=False),
    Column("company", String(63), nullable=False),
    Column("city", String(63), nullable=False),
    Column("state", String(7), nullable=False),
    Column("interests", String(7), nullable=True),
    Column("submitted_date", Date, nullable=False),
    Column("comments", String(255), nullable=True),
)

conferences = Table(
    "conferences",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(100), nullable=True),
    Column("active", Boolean(), autoincrement=False, nullable=False),
    Column("date", Date, nullable=False),
    Column("price", Float(precision=3), autoincrement=False, nullable=False),
    Column("address", String(300)),
)


def start_mappers():
    logger.info("Starting mappers")
    mapper_registry.map_imperatively(model.Notification, notifications)
    mapper_registry.map_imperatively(model.Attendee, attendees)
    mapper_registry.map_imperatively(model.Conference, conferences)
