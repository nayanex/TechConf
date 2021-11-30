from __future__ import annotations

from datetime import date


class Notification:
    def __init__(
        self,
        status: str,
        message: str,
        subject: str,
        submitted_date: str = None,
        completed_date: str = None,
    ):
        self.status = status
        self.message = message
        self.subject = subject
        self.submitted_date = submitted_date
        self.completed_date = completed_date


class Attendee:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        conference_id: int,
        job_position: str,
        email: str,
        company: str,
        city: str,
        state: str,
        submitted_date: date,
        interests: str = None,
        comments: str = None,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.conference_id = conference_id
        self.job_position = job_position
        self.email = email
        self.company = company
        self.state = state
        self.city = city
        self.submitted_date = submitted_date
        self.interests = interests
        self.comments = comments

    def __repr__(self):
        return f"<Attendee {self.first_name}>"


class Conference:
    def __init__(
        self,
        name: str,
        active: bool,
        date: date,
        price: float,
        address: str,
    ):
        self.name = name
        self.active = active
        self.date = date
        self.price = price
        self.address = address
