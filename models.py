"""Models for Pets."""

from flask_sqlalchemy import SQLAlchemy
print("MODELS.PY")

db = SQLAlchemy()


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

    __tablename__ = "pets"


    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True)

    name = db.Column(
        db.String(50),
        nullable=False)

    species = db.Column(
        db.String(100),
        nullable=False)

    photo_url = db.Column(
        db.Text,
        nullable=False,
        default="")

    age = db.Column(
        db.String(50),
        nullable=False)

    notes = db.Column(
        db.Text,
        nullable=False,
        default="")

    available = db.Column(
        db.Boolean,
        nullable=False,
        default=True)
    

print("MODELS-END.PY")