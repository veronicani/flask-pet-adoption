"""Seed file to make sample data for pets database."""
print("SEED.PY")
from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# Add pets
whiskey = Pet(name="Whiskey", species="dog", photo_url="", age="senior")
fluffy = Pet(name="Fluffy", species="cat", photo_url="", age="young")
mustache = Pet(name="Mustache", species="porcupine",
               photo_url="", age="adult", available=False)

# Add pets to the session
db.session.add(whiskey)
db.session.add(fluffy)
db.session.add(mustache)

db.session.commit()

print("END SEED.PY")