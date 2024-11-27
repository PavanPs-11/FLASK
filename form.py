from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField, SelectField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    name = StringField("Enter Your Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    gender = RadioField("Gender", choices=[("M", "Male"), ("F", "Female")])
    languages = SelectField("Languages", choices=[("cpp", "C++"), ("python", "Python")])
    submit = SubmitField("Log In")
