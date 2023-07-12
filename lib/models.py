# Author: Sakthi Santhosh
# Created on: 22/04/2023
from lib import db_handle

class Responder(db_handle.Model):
    guid = db_handle.Column(
        db_handle.Integer,
        primary_key=True
    )
    first_name = db_handle.Column(
        db_handle.String(50),
        unique=False,
        nullable=False
    )
    last_name = db_handle.Column(
        db_handle.String(50),
        unique=False,
        nullable=False
    )
    email_id = db_handle.Column(
        db_handle.String(50),
        unique=True,
        nullable=False
    )
    phone = db_handle.Column(
        db_handle.String(15),
        unique=True,
        nullable=False
    )

    def __repr__(self):
        return f"<Responder {self.first_name} {self.last_name} ({self.email_id})>"

class Event(db_handle.Model):
    guid = db_handle.Column(
        db_handle.Integer,
        primary_key=True
    )
    datetime = db_handle.Column(
        db_handle.DateTime(timezone=True),
        unique=False,
        nullable=False
    )
    device_id = db_handle.Column(
        db_handle.String(36),
        unique=False,
        nullable=False
    )
    prediction = db_handle.Column(
        db_handle.Float,
        unique=False,
        nullable=False
    )
    image = db_handle.Column(
        db_handle.Text
    )

    def __repr__(self):
        return f"<Event {self.datetime} {self.device_id} ({self.prediction})>"

class Device(db_handle.Model):
    guid = db_handle.Column(
        db_handle.Integer,
        primary_key=True
    )
    device_id = db_handle.Column(
        db_handle.String(36),
        unique=True,
        nullable=False
    )
    name = db_handle.Column(
        db_handle.String(30),
        unique=True,
        nullable=False
    )
    latitude = db_handle.Column(
        db_handle.Float,
        unique=False,
        nullable=False
    )
    longitude = db_handle.Column(
        db_handle.Float,
        unique=False,
        nullable=False
    )
    last_updated = db_handle.Column(
        db_handle.DateTime(timezone=True),
        unique=False,
        nullable=True
    )

    def __repr__(self):
        return f"<Device {self.device_id} ({self.name})>"
