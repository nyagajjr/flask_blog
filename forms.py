from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import EqualTo, length, DataRequired

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),length(min=2, max=15)])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm_password', validators=[DataRequired(),EqualTo(password)])