from flask.ext.wtf import FlaskForm,RecaptchaField
from wtforms import TextField,PasswordField,BooleanField
from wtforms.validators import Required,EqualTo,Email

class LoginForm(FlaskForm):
  email=TextField('Email address',[Required(),Email()]) 
  password=PasswordField('Password',[Required()])

class RegisterForm(FlaskForm):
  email=TextField('Email address',[Required(),Email()])
  password=PasswordField('Password',[Required()])
  confirm=PasswordField('Repeat Password',[
  Required(),
  EqualTo('password',message='Passwords must match')
  ])
  accept_tos=BooleanField('I accept the TOS',[Required()])