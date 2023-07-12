# Author: Sakthi Santhosh
# Created on: 22/04/2023
from flask_wtf import FlaskForm
from wtforms import EmailField, FloatField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError

from lib.models import Device, Responder

class AddResponder(FlaskForm):
    first_name = StringField(
        label="First Name",
        validators=[DataRequired(), Length(min=1, max=50)]
    )
    last_name = StringField(
        label="Last Name",
        validators=[DataRequired(), Length(min=1, max=50)]
    )
    email_id = EmailField(
        label="Email ID",
        validators=[DataRequired(), Length(min=1, max=50)]
    )
    phone = StringField(
        label="Phone",
        validators=[DataRequired(), Length(min=4, max=15)]
    )
    submit = SubmitField("Submit")

    def validate_email_id(self, email_id):
        if Responder.query.filter_by(email_id=email_id.data).first():
            raise ValidationError("An responder with the mentioned email ID already exists.")

    def validate_phone(self, phone):
        if Responder.query.filter_by(phone=phone.data).first():
            raise ValidationError("An responder with the mentioned phone # already exists.")

class AddDevice(FlaskForm):
    name = StringField(
        label="Name",
        validators=[DataRequired(), Length(min=1, max=30)]
    )
    longitude = FloatField(
        label="Longitude",
        validators=[DataRequired(), NumberRange(min=-180, max=180)]
    )
    latitude = FloatField(
        label="Latitude",
        validators=[DataRequired(), NumberRange(min=-90, max=90)]
    )
    submit = SubmitField("Submit")

    def validate_name(self, name):
        if Device.query.filter_by(name=name.data).first():
            raise ValidationError("This name is already taken. Please choose a different name.")
