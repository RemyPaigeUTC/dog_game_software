from pprint import pprint

from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user
import sqlalchemy as sa
from app import app, db
from app.models import User, Post, Dog
from app.forms import LoginForm, AddDogForm
from app import utilities

@app.route('/')
def index():
    # Creating webpage using Jinja
    # app/templates
    return render_template('index.html', title='Home')


@app.route('/add_dog', methods=['GET', 'POST'])
def add_dog():
    form = AddDogForm()
    if form.validate_on_submit():
        dog = Dog()
        db.session.add(dog)
        dog.id = form.id.data
        dog.breed = form.breed.data
        dog.gender = form.gender.data
        db.session.commit()
        # Parse Health Data
        # try:
        dog = utilities.parse_health_from_html(form.health_data.data, dog)
        # TODO: Add score to health
        db.session.commit()
        # except:
        #     print("empty health data")

        # Parse Conformation Data
        # try:
        dog = utilities.parse_conformation_from_html(form.conformation_data.data, dog)
        # TODO: Add score to conf
        db.session.commit()
        # except:
        #     print("empty conformation data")
        # Create registered name
        dog.registered_name = utilities.registered_name_from_id(dog.id)
        # find parent IDs from regsitered names
        #parents don't exist for gen 0s
        if bool(form.parent1_registered_name.data):
            parent1_id = utilities.id_from_registered_name(form.parent1_registered_name.data)
            parent2_id = utilities.id_from_registered_name(form.parent2_registered_name.data)
            parent1 = db.session.scalar(sa.select(Dog).where(Dog.id == parent1_id))
            parent2 = db.session.scalar(sa.select(Dog).where(Dog.id == parent2_id))
            parent1.become_parent_to(dog)
            parent2.become_parent_to(dog)

        pprint(vars(dog))
        db.session.commit()
        return redirect(url_for('view_dog', id=dog.id))
    else:
        # dont forget to pass the form in
        return render_template("add_dog.html", title='Add Dog', form=form)

@app.route('/view_dog/<id>', methods=['GET', 'POST'])
def view_dog(id):
    trait_list = ['muzzle_length', 'muzzle_depth', 'dewlap', 'brow_ridge', 'profile', 'bite', 'skull', 'head_width', 'stop',
     'head_carriage', 'ear_ser', 'ear_length', 'ear_width', 'ear_points', 'ear_carriage', 'eye_size', 'eye_shape',
     'bone', 'build', 'back_length', 'back_shape', 'topline', 'neck_length', 'croup', 'chest_depth', 'chest_width',
     'tuck', 'wrinkle', 'leg_length', 'front_angulation', 'rear_angulation', 'reach', 'drive', 'pasterns', 'feet',
     'hind_dew_claws', 'tail_shape', 'tail_length', 'tail_set', 'tail_carriage', 'hairless', 'coat_length',
     'furnishings', 'topknot', 'ear_fringe_type', 'ear_fringe_length', 'neck_ruff', 'body_coat', 'leg_feather',
     'tail_plume', 'coat_curl', 'texture', 'undercoat', 'coat_lay', 'ridge', 'shedding', 'coat_type_genotype',
     'eye_colour', 'pigment', 'nose_colour', 'coat_colour_genotype', 'coat_colour']
    affected_health_values = ["Phenotype Affected", "Genotype Carrier", "Genotype Affected", "Genotype Affected Carrying Clear"]
    dog = db.first_or_404(sa.select(Dog).where(Dog.id == id))
    dog_basic = {}
    dog_health = {}
    dog_conformation = {}

    for attr, value in dog.__dict__.items():
        if value is not None or value != "None":
            if attr == "id" or attr == "breed" or attr == "gender" or attr == "registered_name":
                dog_basic[attr] = value
            elif attr == "health_score":
                dog_health[attr] = value
            elif attr == "conformation_score":
                dog_conformation[attr] = value
            elif attr in trait_list:
                dog_conformation[attr] = value
            elif value in affected_health_values:
                dog_health[attr] = value

    return render_template("view_dog.html", title="View Dog", dog_basic=dog_basic, dog_health=dog_health, dog_conformation=dog_conformation)



# Acceot GET and POST requests in same function
@app.route('/login', methods=['GET', 'POST'])
def login():
    # POST request
    # redirect if currently logged-in user tries to log in
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    # create form object to pass to template
    form = LoginForm()

    # This is false on a GET request
    # runs validators and returns true if OK
    if form.validate_on_submit():
        # scalar used - returns object or none - there is only one
        # username and password from form
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            # show message to user
            flash('Invalid username or password')
            return redirect(url_for('login'))
        # if the username and password is right, login_user from flask login is run then redirect
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
