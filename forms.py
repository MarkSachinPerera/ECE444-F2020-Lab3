from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, Regexp
from wtforms import StringField, SubmitField

class submitForm(FlaskForm):
    name = StringField("Enter your name?", validators=[DataRequired()])
    email = StringField("Enter your UofT email address?", validators=[Email(granular_message=True)])
    submit = SubmitField("Submit")