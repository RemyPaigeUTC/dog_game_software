from pprint import pprint

from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user
import sqlalchemy as sa
from app import app, db
from app.models import User, Post, Dog
from app.forms import LoginForm, AddDogForm
from app import utilities
from app.utilities import create_dog_dict, create_descendant_disease_dict, list_descendants_diseases, \
    list_unique_descendants_diseases, create_count_descendants_dict, create_descendant_dict_ggp

# TODO: code filters
# TODO: improve look of overflowing small health boxes
# TODO: add conformation onto index with toggle switch
# TODO: make the form look nicer
# TODO: improve conformation score
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
    truncated_attrs_dict = {
     'Cavalier King Charles Spaniel': 'CaKiChSp',
     'Cavalier_King_Charles_Spaniel': 'CaKiChSp',
     'Jack Russell Terrier': 'JaRuTe',
     'Jack_Russell_Terrier': 'JaRuTe',
     'addisons_disease': 'AdDi',
     'atopy': 'At',
     'autoimmune_thyroid_disease': 'AuThDi',
     'back_length': 'BaLe',
     'back_shape': 'BaSh',
     'bite': 'Bi',
     'body_coat': 'BoCo',
     'bone': 'Bo',
     'brow_ridge': 'BrRi',
     'build': 'Bu',
     'cardiomyopathy': 'Ca',
     'cervical_spondylomyelopathy': 'CeSp',
     'chest_depth': 'ChDe',
     'chest_width': 'ChWi',
     'chiari_malformation': 'ChMa',
     'chondrodystrophy': 'Ch',
     'chronic_hepatitis': 'ChHe',
     'cleft_palate': 'ClPa',
     'coat_colour': 'CoCo',
     'coat_colour_genotype': 'CoCoGe',
     'coat_curl': 'CoCu',
     'coat_lay': 'CoLa',
     'coat_length': 'CoLe',
     'coat_type_genotype': 'CoTyGe',
     'corneal_dystrophy': 'CoDy',
     'croup': 'Cr',
     'cryptorchidism': 'Cr',
     'deafness_congenital': 'DeCo',
     'degenerative_myelopathy': 'DeMy',
     'demodicosis': 'De',
     'dewlap': 'De',
     'diabetes_mellitus': 'DiMe',
     'dilated_cardiomyopathy': 'DiCa',
     'distichiasis': 'Di',
     'drive': 'Dr',
     'ear_carriage': 'EaCa',
     'ear_fringe_length': 'EaFrLe',
     'ear_fringe_type': 'EaFrTy',
     'ear_length': 'EaLe',
     'ear_points': 'EaPo',
     'ear_ser': 'EaSe',
     'ear_width': 'EaWi',
     'elbow_dysplasia': 'ElDy',
     'endocardiosis': 'En',
     'entropion': 'En',
     'epilepsy': 'Ep',
     'exocrine_pancreatic_insufficiency': 'ExPaIn',
     'eye_colour': 'EyCo',
     'eye_shape': 'EySh',
     'eye_size': 'EySi',
     'feet': 'Fe',
     'front_angulation': 'FrAn',
     'furnishings': 'Fu',
     'hairless': 'Ha',
     'head_carriage': 'HeCa',
     'head_width': 'HeWi',
     'hind_dew_claws': 'HiDeCl',
     'hip_dysplasia': 'HiDy',
     'hydrocephalus': 'Hy',
     'ichthyosis': 'Ic',
     'keratoconjunctivitis_sicca': 'KeSi',
     'leg_feather': 'LeFe',
     'leg_length': 'LeLe',
     'legg_calve_perthes_disease': 'LeCaPeDi',
     'microphthalmia': 'Mi',
     'mitral_valve_dysplasia': 'MiVaDy',
     'muscular_dystrophy': 'MuDy',
     'muzzle_depth': 'MuDe',
     'muzzle_length': 'MuLe',
     'myotonia_congenita': 'MyCo',
     'neck_length': 'NeLe',
     'neck_ruff': 'NeRu',
     'nose_colour': 'NoCo',
     'pasterns': 'Pa',
     'patellar_luxation': 'PaLu',
     'patent_ductus_arteriosus': 'PaDuAr',
     'persistent_pupillary_membranes': 'PePuMe',
     'pigment': 'Pi',
     'primary_glomerulopathy': 'PrGl',
     'profile': 'Pr',
     'progressive_retinal_atrophy': 'PrReAt',
     'protein_losing_enteropathy': 'PrLoEn',
     'pulmonic_stenosis': 'PuSt',
     'reach': 'Re',
     'rear_angulation': 'ReAn',
     'retinal_dysplasia': 'ReDy',
     'ridge': 'Ri',
     'shedding': 'Sh',
     'skull': 'Sk',
     'stop': 'St',
     'tail_carriage': 'TaCa',
     'tail_length': 'TaLe',
     'tail_plume': 'TaPl',
     'tail_set': 'TaSe',
     'tail_shape': 'TaSh',
     'texture': 'Te',
     'topknot': 'To',
     'topline': 'To',
     'tuck': 'Tu',
     'umbilical_hernia': 'UmHe',
     'undercoat': 'Un',
     'urolithiasis': 'Ur',
     'ventricular_septal_defect': 'VeSeDe',
     'vitreous_degeneration': 'ViDe',
     'wrinkle': 'Wr'}
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
        unique_descendants_diseases = list_unique_descendants_diseases(dog)
        for disease in unique_descendants_diseases:
            dog_dict["health"][disease] = "Descendant"
        all_dogs_dict[dog.id] = dog_dict


    # return render_template('index.html', title='Home', dogs=all_dogs_dict, next_url=next_url, prev_url=prev_url)
    return render_template('index.html', title='Home', dogs=all_dogs_dict, truncated_attrs_dict=truncated_attrs_dict)

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
        try:
            dog = utilities.parse_health_from_html(form.health_data.data, dog)
            db.session.commit()
        except:
            print("empty health data")

        # Parse Conformation Data
        try:
            dog = utilities.parse_conformation_from_html(form.conformation_data.data, dog)
            db.session.commit()
        except:
            print("empty conformation data")

        # Additional Info
        dog.generation = utilities.calculate_generation(dog, 1)
        dog.health_score = utilities.calculate_health_score(dog)
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

        db.session.commit()
        return redirect(url_for('view_dog', id=dog.id))
    else:
        # dont forget to pass the form in
        return render_template("add_dog.html", title='Add Dog', form=form)

@app.route('/edit_dog/<id>', methods=['GET', 'POST'])
def edit_dog(id):
    form = AddDogForm()
    if form.validate_on_submit():
        dog = db.first_or_404(sa.select(Dog).where(Dog.id == id))
        dog.living_status = form.living_status.data
        dog.breed = form.breed.data
        dog.gender = form.gender.data
        db.session.commit()
        # Parse Health Data
        try:
            dog = utilities.parse_health_from_html(form.health_data.data, dog)
            db.session.commit()
        except:
            print("empty health data")

        # Parse Conformation Data
        try:
            dog = utilities.parse_conformation_from_html(form.conformation_data.data, dog)
            db.session.commit()
        except:
            print("empty conformation data")

        # Additional Info
        dog.generation = utilities.calculate_generation(dog, 1)
        dog.health_score = utilities.calculate_health_score(dog)
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

        db.session.commit()
        return redirect(url_for('view_dog', id=dog.id))
    elif request.method == 'GET':
        dog = db.first_or_404(sa.select(Dog).where(Dog.id == id))
        form.id.data = id
        form.living_status.data = dog.living_status
        form.breed.data = dog.breed
        form.gender.data = dog.gender

        if dog.list_parents():
            form.parent1_registered_name.data = dog.list_parents()[0].registered_name
            form.parent2_registered_name.data = dog.list_parents()[1].registered_name
        return render_template("edit_dog.html", title='Edit Dog', form=form)
    else:
        # dont forget to pass the form in
        return render_template("add_dog.html", title='Add Dog', form=form)

@app.route('/view_dog/<id>', methods=['GET', 'POST'])
def view_dog(id):
    truncated_attrs_dict = {'Cavalier_King_Charles_Spaniel': 'CaKiChSp',
     'Jack_Russell_Terrier': 'JaRuTe',
     'addisons_disease': 'AdDi',
     'atopy': 'At',
     'autoimmune_thyroid_disease': 'AuThDi',
     'back_length': 'BaLe',
     'back_shape': 'BaSh',
     'bite': 'Bi',
     'body_coat': 'BoCo',
     'bone': 'Bo',
     'brow_ridge': 'BrRi',
     'build': 'Bu',
     'cardiomyopathy': 'Ca',
     'cervical_spondylomyelopathy': 'CeSp',
     'chest_depth': 'ChDe',
     'chest_width': 'ChWi',
     'chiari_malformation': 'ChMa',
     'chondrodystrophy': 'Ch',
     'chronic_hepatitis': 'ChHe',
     'cleft_palate': 'ClPa',
     'coat_colour': 'CoCo',
     'coat_colour_genotype': 'CoCoGe',
     'coat_curl': 'CoCu',
     'coat_lay': 'CoLa',
     'coat_length': 'CoLe',
     'coat_type_genotype': 'CoTyGe',
     'corneal_dystrophy': 'CoDy',
     'croup': 'Cr',
     'cryptorchidism': 'Cr',
     'deafness_congenital': 'DeCo',
     'degenerative_myelopathy': 'DeMy',
     'demodicosis': 'De',
     'dewlap': 'De',
     'diabetes_mellitus': 'DiMe',
     'dilated_cardiomyopathy': 'DiCa',
     'distichiasis': 'Di',
     'drive': 'Dr',
     'ear_carriage': 'EaCa',
     'ear_fringe_length': 'EaFrLe',
     'ear_fringe_type': 'EaFrTy',
     'ear_length': 'EaLe',
     'ear_points': 'EaPo',
     'ear_ser': 'EaSe',
     'ear_width': 'EaWi',
     'elbow_dysplasia': 'ElDy',
     'endocardiosis': 'En',
     'entropion': 'En',
     'epilepsy': 'Ep',
     'exocrine_pancreatic_insufficiency': 'ExPaIn',
     'eye_colour': 'EyCo',
     'eye_shape': 'EySh',
     'eye_size': 'EySi',
     'feet': 'Fe',
     'front_angulation': 'FrAn',
     'furnishings': 'Fu',
     'hairless': 'Ha',
     'head_carriage': 'HeCa',
     'head_width': 'HeWi',
     'hind_dew_claws': 'HiDeCl',
     'hip_dysplasia': 'HiDy',
     'hydrocephalus': 'Hy',
     'ichthyosis': 'Ic',
     'keratoconjunctivitis_sicca': 'KeSi',
     'leg_feather': 'LeFe',
     'leg_length': 'LeLe',
     'legg_calve_perthes_disease': 'LeCaPeDi',
     'microphthalmia': 'Mi',
     'mitral_valve_dysplasia': 'MiVaDy',
     'muscular_dystrophy': 'MuDy',
     'muzzle_depth': 'MuDe',
     'muzzle_length': 'MuLe',
     'myotonia_congenita': 'MyCo',
     'neck_length': 'NeLe',
     'neck_ruff': 'NeRu',
     'nose_colour': 'NoCo',
     'pasterns': 'Pa',
     'patellar_luxation': 'PaLu',
     'patent_ductus_arteriosus': 'PaDuAr',
     'persistent_pupillary_membranes': 'PePuMe',
     'pigment': 'Pi',
     'primary_glomerulopathy': 'PrGl',
     'profile': 'Pr',
     'progressive_retinal_atrophy': 'PrReAt',
     'protein_losing_enteropathy': 'PrLoEn',
     'pulmonic_stenosis': 'PuSt',
     'reach': 'Re',
     'rear_angulation': 'ReAn',
     'retinal_dysplasia': 'ReDy',
     'ridge': 'Ri',
     'shedding': 'Sh',
     'skull': 'Sk',
     'stop': 'St',
     'tail_carriage': 'TaCa',
     'tail_length': 'TaLe',
     'tail_plume': 'TaPl',
     'tail_set': 'TaSe',
     'tail_shape': 'TaSh',
     'texture': 'Te',
     'topknot': 'To',
     'topline': 'To',
     'tuck': 'Tu',
     'umbilical_hernia': 'UmHe',
     'undercoat': 'Un',
     'urolithiasis': 'Ur',
     'ventricular_septal_defect': 'VeSeDe',
     'vitreous_degeneration': 'ViDe',
     'wrinkle': 'Wr'}
    dog = db.first_or_404(sa.select(Dog).where(Dog.id == id))
    dog_dict = utilities.create_dog_dict(dog)
    descendant_disease_dict = create_descendant_disease_dict(dog, 1, {})
    unique_descendants_diseases = list_unique_descendants_diseases(dog)
    count_descendants_dict = create_count_descendants_dict(dog, 1, {})
    descendant_dict_ggp = create_descendant_dict_ggp(dog)
    return render_template("view_dog.html",
                           title="View Dog",
                           dog_basic=dog_dict["basic"],
                           dog_health=dog_dict["health"],
                           dog_conformation=dog_dict["conformation"],
                           truncated_attrs_dict=truncated_attrs_dict,
                           descendant_disease_dict=descendant_disease_dict,
                           unique_descendants_diseases=unique_descendants_diseases,
                           count_descendants_dict=count_descendants_dict,
                           descendant_dict_ggp=descendant_dict_ggp)

# Accept GET and POST requests in same function
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
