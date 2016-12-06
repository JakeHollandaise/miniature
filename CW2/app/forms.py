from flask_wtf import FlaskForm
from wtforms import  BooleanField, StringField, PasswordField, validators
from wtforms.fields.html5 import URLField
from wtforms.validators import url


class shortenerForm(FlaskForm):
	longURL = URLField('url', validators = [url()])

#registration for session
class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])


#login form for session
class loginForm(FlaskForm):
	username = StringField('username', [validators.Length(min=4, max=25), validators.DataRequired()])
	password = PasswordField('password', [validators.DataRequired()])
	remember_me = BooleanField('remember_me', default=False)
