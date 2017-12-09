from flask.ext.wtf import FlaskForm,RecaptchaField
from wtforms import TextField,PasswordField,BooleanField
from wtforms.validators import Required,EqualTo,Email

class NotesForm(FlaskForm):
  title=TextField('Title',[Required()])
  body=TextField('Body',[Required()])