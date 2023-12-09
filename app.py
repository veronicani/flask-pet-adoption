import os

from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

from forms import AddPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///pet_adoption")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'i-have-a-secret'

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)
toolbar = DebugToolbarExtension(app)

print("app.config.url: ", app.config['SQLALCHEMY_DATABASE_URI'])

@app.get('/')
def show_pets():
    """Homepage displays all pets."""

    pets = Pet.query.order_by(Pet.name).all()
    print("pets: ", pets)

    return render_template('homepage.html', pets=pets)



@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Pet add form; handle adding."""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name,
                    species=species,
                    photo_url=photo_url,
                    age=age,
                    notes=notes)

        db.session.add(new_pet)
        db.session.commit()

        #TODO:flash message

        flash(f"Added {name}")
        return redirect("/")

    else:
        return render_template(
            "pet_add_form.html", form=form)