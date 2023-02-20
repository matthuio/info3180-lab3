from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import (InputRequired,Email)

class ContactForm(FlaskForm):
    name = StringField('Name',validators=[InputRequired(message= "Please enter your first and last name")])
    email = StringField('Email',validators=[Email(message = 'Please enter a valid email'),InputRequired(message= "Please eneter your email address")])
    subject = StringField('Subject',validators=[InputRequired(message="Please enter a message")])
    message = StringField('Message', render_kw={"rows": 8, "cols": 50})