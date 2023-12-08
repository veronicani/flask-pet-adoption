from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SelectField

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name")
    species = StringField("Species Name")
    photo_url = StringField("Photo Url")
    age = SelectField('Age',
                      choices=[('baby','Baby'),
                            ('young','Young'),
                            ('adult','Adult'),
                            ('senior','Senior')])
    notes = StringField("Notes")
