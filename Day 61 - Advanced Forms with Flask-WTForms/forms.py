from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo
import email_validator


# class RegistrationForm(FlaskForm):
#     email = StringField('Email',
#                         validators=[DataRequired(), Length(min=4, max=30), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     confirm_password = PasswordField('Confirm Password',
#                                      validators=[DataRequired(), EqualTo('password')])
#     submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(message="Invalid email format")])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')