from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField(
        "Pet Name",
        validators=[InputRequired()])
    species = SelectField(
        "Species Name",
        choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')],
        validators=[InputRequired()])
    photo_url = StringField(
        "Photo Url",
        validators=[Optional(), URL()])
    age = SelectField('Age',
                      choices=[('baby', 'Baby'),
                               ('young', 'Young'),
                               ('adult', 'Adult'),
                               ('senior', 'Senior')],
                      validators=[InputRequired()])
    notes = StringField(
        "Notes",
        validators=[Optional()])


class EditPetForm(FlaskForm):

    photo_url = StringField(
        "Photo Url",
        validators=[Optional(), URL()])
    notes = StringField(
        "Notes",
        validators=[Optional()])
    available = BooleanField(
        "Available?",
        validators=[Optional()])
