from pprint import pprint

from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user
import sqlalchemy as sa
from app import app, db
from app.models import User, Post, Dog
from app.forms import LoginForm, AddDogForm
from app import utilities
from app.utilities import create_dog_dict


@app.route('/')
def index():
    genotypes_list = ["dilated_cardiomyopathy", "cardiomyopathy", "progressive_retinal_atrophy", "retinal_dysplasia",
                      "chondrodystrophy", "muscular_dystrophy", "myotonia_congenita", "degenerative_myelopathy",
                      "ichthyosis", "primary_glomerulopathy",
                      "urolithiasis"]
    phenotypes_list = ["endocardiosis", "chiari_malformation", "deafness_congenital", "mitral_valve_dysplasia",
                       "patent_ductus_arteriosus",
                       "pulmonic_stenosis", "ventricular_septal_defect", "corneal_dystrophy", "distichiasis",
                       "keratoconjunctivitis_sicca",
                       "exocrine_pancreatic_insufficiency", "cervical_spondylomyelopathy", "elbow_dysplasia",
                       "hip_dysplasia", "patellar_luxation",
                       "epilepsy", "atopy", "umbilical_hernia", "addisons_disease", "autoimmune_thyroid_disease",
                       "diabetes_mellitus",
                       "entropion", "microphthalmia", "persistent_pupillary_membranes", "vitreous_degeneration",
                       "protein_losing_enteropathy",
                       "legg_calve_perthes_disease", "hydrocephalus", "cleft_palate", "demodicosis", "cryptorchidism",
                       "chronic_hepatitis"]
    # Creating webpage using Jinja
    # app/templates
    page = request.args.get('page', 1, type=int)
    query = sa.select(Dog).where(Dog.living_status == "alive").order_by(Dog.id.asc())
    # posts = db.session.scalars(current_user.following_posts()).all()
    dogs = db.session.scalars(query).all()
    # dogs = db.paginate(query, page=page, per_page=app.config['DOGS_PER_PAGE'], error_out=False)
    # next_url = url_for('index', page=dogs.next_num) \
    #     if dogs.has_next else None
    # prev_url = url_for('index', page=dogs.prev_num) \
    #     if dogs.has_prev else None
    # id:   basic:
    #       health:
    #       conf:
    all_dogs_dict = {}
    for dog in dogs:
        dog_dict = create_dog_dict(dog)
        all_dogs_dict[dog.id] = dog_dict
    for dog in all_dogs_dict.values():
        for attr, value in dog["health"].copy().items():
            try:
                if "Clear" in value:
                    value = "#479f76"
                elif "Affected" in value:
                    value = "#ea868f"
                elif "Carrier" in value:
                    value = "#feb272"
                else:
                    value = "#000000"
            except:
                value = "#000000"
            first_letters = "".join(x[0] for x in attr.split("_")).upper()
            second_letters = "".join(x[1] for x in attr.split("_"))
            first_and_second_letters = ''.join(''.join(x) for x in zip(first_letters, second_letters))
            dog["health"][first_and_second_letters] = value
            del dog["health"][attr]

    # return render_template('index.html', title='Home', dogs=all_dogs_dict, next_url=next_url, prev_url=prev_url)
    return render_template('index.html', title='Home', dogs=all_dogs_dict)

@app.route('/add_dog', methods=['GET', 'POST'])
def add_dog():
    form = AddDogForm()
    if form.validate_on_submit():
        dog = Dog()
        db.session.add(dog)
        dog.id = form.id.data
        dog.living_status = form.living_status.data
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
        # TODO: Add generation calculation

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
    dog = db.first_or_404(sa.select(Dog).where(Dog.id == id))
    dog_dict = utilities.create_dog_dict(dog)
    return render_template("view_dog.html", title="View Dog", dog_basic=dog_dict["basic"], dog_health=dog_dict["health"], dog_conformation=dog_dict["conformation"])



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
