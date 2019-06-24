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

class loginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=2, max=30)])
    password = PasswordField('password', validators=[DataRequired(), Length(min=2, max=30)])
    submit = SubmitField('login')

class registration(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=2, max=30)])
    password = PasswordField('password', validators=[DataRequired(), Length(min=2, max=30)])
    emailAddress = StringField('Email Address', validators=[DataRequired(), Email()])
    submit = SubmitField('Register')

class forgotPassword(FlaskForm):
        email= StringField('Email Address', validators=[DataRequired(), Email()])
        submit = SubmitField('Send Email')

class PasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])

class viewItems(FlaskForm):
    itemCategory = SelectField('itemCategory',   choices=[('cable_basket', 'Cable Basket'), ('cable_Ladder', 'Cable Ladder'),
                                                         ('cable_tray', 'Cable Tray'), ('cable_trunking', 'Cable Trunking'),
                                                         ('channel_support', 'Channel Support'), ('dado_trunking', 'Dado Trunking'),
                                                         ('Floor_Service_Box', 'Floor Service Box'), ('lighting_trunking', 'Lighting Trunking'),
                                                         ('plastic_conduit', 'Plastic Conduit'), ('roof_support_systems', 'Roof Support Systems')], validators=[DataRequired()])
    submit = SubmitField('Choose form')
    

class addModel(FlaskForm):
    itemName = StringField('itemName', validators=[DataRequired(), Length(min=2, max=30)])
    modelRef = StringField('modelRef', validators=[DataRequired(), Length(min=2, max=30)])
    modelNumber = StringField('modelNumber', validators=[DataRequired(), Length(min=2, max=30)])

    itemCategory = SelectField('itemCategory',   choices=[ ('cable_basket', 'Cable Basket'), ('cable_Ladder', 'Cable Ladder'),
                                                         ('cable_tray', 'Cable Tray'), ('cable_trunking', 'Cable Trunking'),
                                                         ('channel_support', 'Channel Support'), ('dado_trunking', 'Dado Trunking'),
                                                         ('Floor_Service_Box', 'Floor Service Box'), ('lighting_trunking', 'Lighting Trunking'),
                                                         ('plastic_conduit', 'Plastic Conduit'), ('roof_support_systems', 'Roof Support Systems')], validators=[DataRequired()])

    itemCategory = SelectField('itemCategory',   choices=[('cable_basket', 'Cable Basket'), ('cable_Ladder', 'Cable Ladder'),
                                                         ('cable_tray', 'Cable Tray'), ('cable_trunking', 'Cable Trunking'),
                                                         ('channel_support', 'Channel Support'), ('dado_trunking', 'Dado Trunking'),
                                                         ('Floor_Service_Box', 'Floor Service Box'), ('lighting_trunking', 'Lighting Trunking'),
                                                         ('plastic_conduit', 'Plastic Conduit'), ('roof_support_systems', 'Roof Support Systems')], validators=[DataRequired()])
    measurements = SelectField('Measurements', choices=[('None', 'None'),('Width', 'Width'), ('Height', 'Height'), ('Length', 'Length'),
                                                        ('Diameter', 'Diameter'), ('Finish', 'Finish'),
                                                        ('Material', 'Material'), ('Size', 'Size'),
                                                        ('Thickeness', 'Thickness'), ('Thread', 'Thread'),
                                                        ('Pack_Quantity', 'Pack Quantity'), 
                                                        ('Box_Quantity', 'Box Quantity'), ('AFXWeight', 'AFX Weight'),
                                                         ('Load_Bearing', 'Load Bearing'), ('Height_With_Foot', 'Height With Foot'), ('Max.Loading', 'Max Loading')], validators=[DataRequired(), Email()])
    value = StringField('value', validators=[DataRequired(), Length(min=2, max=30)])
    measurements2 = SelectField('Measurements', choices=[('None', 'None'),('Width', 'Width'), ('Height', 'Height'), ('Length', 'Length'),
                                                        ('Diameter', 'Diameter'), ('Finish', 'Finish'),
                                                        ('Material', 'Material'), ('Size', 'Size'),
                                                        ('Thickeness', 'Thickness'), ('Thread', 'Thread'),
                                                        ('Pack_Quantity', 'Pack Quantity'), 
                                                        ('Box_Quantity', 'Box Quantity'), ('AFXWeight', 'AFX Weight'),
                                                         ('Load_Bearing', 'Load Bearing'), ('Height_With_Foot', 'Height With Foot'), ('Max.Loading', 'Max Loading')], validators=[DataRequired(), Email()])
    value2 = StringField('value', validators=[DataRequired(), Length(min=2, max=30)])
    measurements3 = SelectField('Measurements', choices=[('None', 'None'),('Width', 'Width'), ('Height', 'Height'), ('Length', 'Length'),
                                                        ('Diameter', 'Diameter'), ('Finish', 'Finish'),
                                                        ('Material', 'Material'), ('Size', 'Size'),
                                                        ('Thickeness', 'Thickness'), ('Thread', 'Thread'),
                                                        ('Pack_Quantity', 'Pack Quantity'), 
                                                        ('Box_Quantity', 'Box Quantity'), ('AFXWeight', 'AFX Weight'),
                                                         ('Load_Bearing', 'Load Bearing'), ('Height_With_Foot', 'Height With Foot'), ('Max.Loading', 'Max Loading')], validators=[DataRequired(), Email()])
    value3 = StringField('value', validators=[DataRequired(), Length(min=2, max=30)])
    measurements4 = SelectField('Measurements', choices=[('None', 'None'),('Width', 'Width'), ('Height', 'Height'), ('Length', 'Length'),
                                                        ('Diameter', 'Diameter'), ('Finish', 'Finish'),
                                                        ('Material', 'Material'), ('Size', 'Size'),
                                                        ('Thickeness', 'Thickness'), ('Thread', 'Thread'),
                                                        ('Pack_Quantity', 'Pack Quantity'), 
                                                        ('Box_Quantity', 'Box Quantity'), ('AFXWeight', 'AFX Weight'),
                                                         ('Load_Bearing', 'Load Bearing'), ('Height_With_Foot', 'Height With Foot'), ('Max.Loading', 'Max Loading')], validators=[DataRequired(), Email()])
    value4 = StringField('value', validators=[DataRequired(), Length(min=2, max=30)])



    submit = SubmitField('Add Entry')


class editModel(FlaskForm):
    itemName = StringField('itemName', validators=[DataRequired(), Length(min=2, max=30)])
    modelRef = StringField('modelRef', validators=[DataRequired(), Length(min=2, max=30)])
    modelNumber = StringField('modelNumber', validators=[DataRequired(), Length(min=2, max=30)])

    itemCategory = SelectField('itemCategory',   choices=[('cable_basket', 'Cable Basket'), ('cable_Ladder', 'Cable Ladder'),
                                                         ('cable_tray', 'Cable Tray'), ('cable_trunking', 'Cable Trunking'),
                                                         ('channel_support', 'Channel Support'), ('dado_trunking', 'Dado Trunking'),
                                                         ('Floor_Service_Box', 'Floor Service Box'), ('lighting_trunking', 'Lighting Trunking'),
                                                         ('plastic_conduit', 'Plastic Conduit'), ('roof_support_systems', 'Roof Support Systems')], validators=[DataRequired()])
    measurements = SelectField('Measurements', choices=[('Width', 'Width'), ('Height', 'Height'), ('Length', 'Length'),
                                                        ('Diameter', 'Diameter'), ('Finish', 'Finish'),
                                                        ('Material', 'Material'), ('Size', 'Size'),
                                                        ('Thickeness', 'Thickness'), ('Thread', 'Thread'),
                                                        ('Pack_Quantity', 'Pack Quantity'), 
                                                        ('Box_Quantity', 'Box Quantity'), ('AFXWeight', 'AFX Weight'),
                                                         ('Load_Bearing', 'Load Bearing'), ('Height_With_Foot', 'Height With Foot'), ('Max.Loading', 'Max Loading')], validators=[DataRequired()])
    value = StringField('value', validators=[DataRequired(), Length(min=2, max=30)])
    measurements2 = SelectField('Measurements', choices=[('None', 'None'),('Width', 'Width'), ('Height', 'Height'), ('Length', 'Length'),
                                                        ('Diameter', 'Diameter'), ('Finish', 'Finish'),
                                                        ('Material', 'Material'), ('Size', 'Size'),
                                                        ('Thickeness', 'Thickness'), ('Thread', 'Thread'),
                                                        ('Pack_Quantity', 'Pack Quantity'), 
                                                        ('Box_Quantity', 'Box Quantity'), ('AFXWeight', 'AFX Weight'),
                                                         ('Load_Bearing', 'Load Bearing'), ('Height_With_Foot', 'Height With Foot'), ('Max.Loading', 'Max Loading')], validators=[DataRequired()])
    value2 = StringField('value', validators=[DataRequired(), Length(min=2, max=30)])
    measurements3 = SelectField('Measurements', choices=[('None', 'None'),('Width', 'Width'), ('Height', 'Height'), ('Length', 'Length'),
                                                        ('Diameter', 'Diameter'), ('Finish', 'Finish'),
                                                        ('Material', 'Material'), ('Size', 'Size'),
                                                        ('Thickeness', 'Thickness'), ('Thread', 'Thread'),
                                                        ('Pack_Quantity', 'Pack Quantity'), 
                                                        ('Box_Quantity', 'Box Quantity'), ('AFXWeight', 'AFX Weight'),
                                                         ('Load_Bearing', 'Load Bearing'), ('Height_With_Foot', 'Height With Foot'), ('Max.Loading', 'Max Loading')], validators=[DataRequired()])
    value3 = StringField('value', validators=[DataRequired(), Length(min=2, max=30)])
    measurements4 = SelectField('Measurements', choices=[('None', 'None'),('Width', 'Width'), ('Height', 'Height'), ('Length', 'Length'),
                                                        ('Diameter', 'Diameter'), ('Finish', 'Finish'),
                                                        ('Material', 'Material'), ('Size', 'Size'),
                                                        ('Thickeness', 'Thickness'), ('Thread', 'Thread'),
                                                        ('Pack_Quantity', 'Pack Quantity'), 
                                                        ('Box_Quantity', 'Box Quantity'), ('AFXWeight', 'AFX Weight'),
                                                         ('Load_Bearing', 'Load Bearing'), ('Height_With_Foot', 'Height With Foot'), ('Max.Loading', 'Max Loading')], validators=[DataRequired()])
    value4 = StringField('value', validators=[DataRequired(), Length(min=2, max=30)])

    submit = SubmitField('Edit Entry')

