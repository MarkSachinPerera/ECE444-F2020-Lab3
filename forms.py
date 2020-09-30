from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email
from wtforms import StringField, SubmitField

class submitForm(FlaskForm):
    name = StringField("Enter your name?", validators=[DataRequired()])
    email = StringField("Enter your U of T email address?", validators=[Email()])
    submit = SubmitField("Submit")