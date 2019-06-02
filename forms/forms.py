from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, IntegerField, \
    FileField, TextField, validators
from wtforms.widgets import TextArea
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp
from wtforms.fields.html5 import DateField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms_components import DateTimeField, DateRange
from flask_bcrypt import Bcrypt, generate_password_hash, check_password_hash
from datetime import datetime, date, timedelta
from flask import session
from wtforms.validators import NumberRange



class registration(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=2, max=30)])
    password = StringField('password', validators=[DataRequired(), Length(min=2, max=30)])
    emailAddress = StringField('Email Address', validators=[DataRequired(), Email()])
    submit = SubmitField('Register')