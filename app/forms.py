from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class AddDogForm(FlaskForm):
    id = IntegerField("Dog ID", validators=[DataRequired()])
    living_status = SelectField("Living Status", choices=[('Alive', "Dead"),("alive", "dead")],
                                                        validators=[DataRequired()])
    breed = SelectField("Dog Breed", choices=[("Cavalier King Charles Spaniel", "Cavalier King Charles Spaniel"),
                                                        ("Jack Russell Terrier", "Jack Russell Terrier")],
                                                        validators=[DataRequired()])
    gender = SelectField("Gender", choices=[("M", "M"), ("F", "F")], validators=[DataRequired()])
    health_data = StringField('Health Data')
    conformation_data = StringField('Conformation Data')
    # personality_data = StringField('Personality Data')
    parent1_registered_name = StringField("Parent Registered Name")
    parent2_registered_name = StringField("Parent Registered Name")
    # activity_data = StringField('Activity Data')
    submit = SubmitField('Add Dog')