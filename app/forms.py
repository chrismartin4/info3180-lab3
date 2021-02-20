from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, validators

class ContactForm(FlaskForm):
    name = StringField('Name', [validators.DataRequired()])
    email = StringField('Email Address', [validators.DataRequired(), validators.Email()])
    subject = StringField('Subject', [validators.DataRequired()])
    message = TextAreaField('Message', [validators.DataRequired()])