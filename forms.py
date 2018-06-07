from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Regexp
from models import db, User
from flask_wtf.file import FileField, FileAllowed, FileRequired

class SignupForm(Form):
  user_name = StringField('User name', validators=[DataRequired("Please enter your username."),Length(min=6,max=10, message="Username must be 6-10 characters or more."),Regexp('^\w+$',message="Username must contain only letters, numbers or underscore")])
  first_name = StringField('First name', validators=[DataRequired("Please enter your first name.")])
  last_name = StringField('Last name', validators=[DataRequired("Please enter your last name.")])
  email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your email address.")])
  password = PasswordField('Password', validators=[DataRequired("Please enter your password."), Length(min=8,max=15, message="Passwords must be 8-15 characters or more."),Regexp('^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$',message="Password must contain at least one letter, one number and one special character")])
  submit = SubmitField('Sign up')

  def validate_user_name(self, field):
        user = User.query.filter(User.username == self.user_name.data).first()
        if user:
            raise ValueError("Sorry.. Username exists")

  def validate_email(self, field):
        user = User.query.filter(User.email == self.email.data).first()
        if user:
            raise ValueError("Sorry.. Email exists")

class LoginForm(Form):
  user_name = StringField('User name', validators=[DataRequired("Please enter your Username.")])
  password = PasswordField('Password', validators=[DataRequired("Please enter your Password.")])
  submit = SubmitField("Sign in")
  def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False
        user = User.query.filter(User.username == self.user_name.data).first()
        if user is None:
            self.user_name.errors.append('Please enter correct credendials.')
            self.password.errors.append('Please enter correct credendials.')
            return False

        if not user.check_password(self.password.data):
            self.user_name.errors.append('Please enter correct credendials.')
            self.password.errors.append('Please enter correct credendials.')
            return False

        self.user = user
        return True


class ForgotPassword(Form):
  user_name = StringField('User name', validators=[DataRequired("Please enter your username.")])
  submit = SubmitField("Enter")
  def validate_user_name(self, field):
        user = User.query.filter(User.username == self.user_name.data).first()
        if user is None:
            self.user_name.errors.append('Please enter correct credendials.')
