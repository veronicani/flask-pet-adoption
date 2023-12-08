"""Models for Pets."""

from flask_sqlalchemy import SQLAlchemy
print("MODELS.PY")

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://tinyurl.com/mry92yn3"


def connect_db(app):
    """Connect to the database."""

    app.app_context().push()
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pets.

        Fields:
            id (Primary Key): Serial num id for pet.
            name: Text. Not NULL.
            species: Text. Not NULL.
            photo_url: Text. Not NULL. Default ''.
            age: Text. Not NULL.
            notes: Text. Not NULL. Default ''.
            available: True/False. Not NULL. Default to True.
    """
