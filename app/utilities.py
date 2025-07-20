import csv
from bs4 import BeautifulSoup
from app.models import Dog
from app import db
import sqlalchemy as sa
from pprint import pprint

def calculate_conf_spaniel(dog):
    perfect_spaniel = {
        "Muzzle Length",
        "Muzzle Depth",
        "Dewlap",
        "Brow Ridge",
        "Profile",
        "Bite",
        "Skull",
        "Head Width",
        "Stop",
        "Head Carriage",
        "Ear Ser",
        "Ear Length",
        "Ear Width",
        "Ear Points",
        "Ear Carriage",
        "Eye Size",
        "Eye Shape",
        "Bone",
        "Build",
        "Back Length",
        "Back Shape",
        "Topline",
        "Neck Length",
        "Croup",
        "Chest Depth",
        "Chest Width",
        "Tuck",
        "Wrinkle",
        "Leg Length",
        "Front Angulation",
        "Rear Angulation",
        "Reach",
        "Drive",
        "Pasterns",
        "Feet",
        "Hind Dew Claws",
        "Tail Shape",
        "Tail Length",
        "Tail Set",
        "Tail Carriage",
        "Hairless",
        "Coat Length",
        "Furnishings",
        "Topknot",
        "Ear Fringe Type",
        "Ear Fringe Length",
        "Neck Ruff",
        "Body Coat",
        "Leg Feather",
        "Tail Plume",
        "Coat Curl",
        "Texture",
        "Undercoat",
        "Coat Lay",
        "Ridge",
        "Shedding",
        "Coat Type Genotype",
        "Eye Colour",
        "Pigment",
        "Nose Colour",
        "Coat Colour Genotype",
        "Coat Colour"
    }

def create_dog_dict(dog):
    trait_list = ['muzzle_length', 'muzzle_depth', 'dewlap', 'brow_ridge', 'profile', 'bite', 'skull', 'head_width',
                  'stop',
                  'head_carriage', 'ear_ser', 'ear_length', 'ear_width', 'ear_points', 'ear_carriage', 'eye_size',
                  'eye_shape',
                  'bone', 'build', 'back_length', 'back_shape', 'topline', 'neck_length', 'croup', 'chest_depth',
                  'chest_width',
                  'tuck', 'wrinkle', 'leg_length', 'front_angulation', 'rear_angulation', 'reach', 'drive', 'pasterns',
                  'feet',
                  'hind_dew_claws', 'tail_shape', 'tail_length', 'tail_set', 'tail_carriage', 'hairless', 'coat_length',
                  'furnishings', 'topknot', 'ear_fringe_type', 'ear_fringe_length', 'neck_ruff', 'body_coat',
                  'leg_feather',
                  'tail_plume', 'coat_curl', 'texture', 'undercoat', 'coat_lay', 'ridge', 'shedding',
                  'coat_type_genotype',
                  'eye_colour', 'pigment', 'nose_colour', 'coat_colour_genotype', 'coat_colour']
    affected_health_values = ["Phenotype Affected", "Genotype Carrier", "Genotype Affected",
                              "Genotype Affected Carrying Clear"]
    basic_attrs = [
        "id", "breed", "gender", "registered_name", "living_status", "gen"
    ]
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
    dog_basic = {}
    dog_health = {}
    dog_conformation = {}

    for attr, value in dog.__dict__.items():
        if value is not None or value != "None" or str(type(value)) != "<class 'NoneType'>":
            if attr in basic_attrs:
                dog_basic[attr] = value
            elif attr in trait_list:
                dog_conformation[attr] = value
            elif value in affected_health_values:
                dog_health[attr] = value
            # elif attr in genotypes_list or attr in phenotypes_list:
            #     dog_health[attr] = value
        else:
            print("None")
    dog_dict = {
        "basic": dog_basic,
        "health": dog_health,
        "conformation": dog_conformation
    }
    print(dog_dict)
    return dog_dict

def id_from_registered_name(registered_name):
    registered_name_string = str(registered_name)
    dog_id_string = ""
    for letter in registered_name_string:
        if letter == "q" or letter == "Q":
            dog_id_string = dog_id_string + "1"
        elif letter == "w" or letter == "W":
            dog_id_string = dog_id_string + "2"
        elif letter == "e" or letter == "E":
            dog_id_string = dog_id_string + "3"
        elif letter == "r" or letter == "R":
            dog_id_string = dog_id_string + "4"
        elif letter == "t" or letter == "T":
            dog_id_string = dog_id_string + "5"
        elif letter == "y" or letter == "Y":
            dog_id_string = dog_id_string + "6"
        elif letter == "u" or letter == "U":
            dog_id_string = dog_id_string + "7"
        elif letter == "i" or letter == "I":
            dog_id_string = dog_id_string + "8"
        elif letter == "o" or letter == "O":
            dog_id_string = dog_id_string + "9"
        elif letter == "p" or letter == "P":
            dog_id_string = dog_id_string + "0"
    dog_id = int(dog_id_string)
    return dog_id

def set_dog_attr(dog, attr, dog_line_value):
    trait_list = ['muzzle_length', 'muzzle_depth', 'dewlap', 'brow_ridge', 'profile', 'bite', 'skull', 'head_width',
                  'stop',
                  'head_carriage', 'ear_ser', 'ear_length', 'ear_width', 'ear_points', 'ear_carriage', 'eye_size',
                  'eye_shape',
                  'bone', 'build', 'back_length', 'back_shape', 'topline', 'neck_length', 'croup', 'chest_depth',
                  'chest_width',
                  'tuck', 'wrinkle', 'leg_length', 'front_angulation', 'rear_angulation', 'reach', 'drive', 'pasterns',
                  'feet',
                  'hind_dew_claws', 'tail_shape', 'tail_length', 'tail_set', 'tail_carriage', 'hairless', 'coat_length',
                  'furnishings', 'topknot', 'ear_fringe_type', 'ear_fringe_length', 'neck_ruff', 'body_coat',
                  'leg_feather',
                  'tail_plume', 'coat_curl', 'texture', 'undercoat', 'coat_lay', 'ridge', 'shedding',
                  'coat_type_genotype',
                  'eye_colour', 'pigment', 'nose_colour', 'coat_colour_genotype', 'coat_colour']
    genotypes_list = ["dilated_cardiomyopathy", "cardiomyopathy", "progressive_retinal_atrophy", "retinal_dysplasia",
                       "chondrodystrophy", "muscular_dystrophy", "myotonia_congenita", "degenerative_myelopathy", "ichthyosis", "primary_glomerulopathy",
                       "urolithiasis"]
    phenotypes_list = ["endocardiosis", "chiari_malformation", "deafness_congenital", "mitral_valve_dysplasia", "patent_ductus_arteriosus",
                       "pulmonic_stenosis", "ventricular_septal_defect", "corneal_dystrophy", "distichiasis", "keratoconjunctivitis_sicca",
                       "exocrine_pancreatic_insufficiency", "cervical_spondylomyelopathy", "elbow_dysplasia", "hip_dysplasia", "patellar_luxation",
                       "epilepsy", "atopy", "umbilical_hernia", "addisons_disease", "autoimmune_thyroid_disease", "diabetes_mellitus",
                       "entropion", "microphthalmia", "persistent_pupillary_membranes", "vitreous_degeneration", "protein_losing_enteropathy",
                       "legg_calve_perthes_disease", "hydrocephalus", "cleft_palate","demodicosis","cryptorchidism","chronic_hepatitis"]
    if dog_line_value == "":
        setattr(dog, attr, "None")
    elif attr in genotypes_list:
        dog_line_value = int(dog_line_value)
        if dog_line_value == 0:
            setattr(dog, attr, "Genotype Affected")
        elif dog_line_value == 1:
            setattr(dog, attr, "Genotype Carrier")
        elif dog_line_value == 2:
            setattr(dog, attr, "Genotype Clear")
    elif attr in phenotypes_list:
        dog_line_value = int(dog_line_value)
        if dog_line_value == 0:
            setattr(dog, attr, "Phenotype Affected")
        elif dog_line_value == 2:
            setattr(dog, attr, "Phenotype Clear")

    return dog

def parse_csv():
    with open("html_parser/dog_base.csv") as fp:
        reader = csv.reader(fp, delimiter=",", quotechar='"')
        # next(reader, None)  # skip the headers
        data_read = [row for row in reader]

    data_columns = [ "dilated_cardiomyopathy", "cardiomyopathy", "progressive_retinal_atrophy", "retinal_dysplasia",
                    "chondrodystrophy", "muscular_dystrophy", "myotonia_congenita", "degenerative_myelopathy", "ichthyosis", "primary_glomerulopathy",
                     "urolithiasis",
    ]
    for dog_line in data_read:
        dog = Dog()
        db.session.add(dog)
        for i in range(len(dog_line)):
            if i == 0:
                dog.id = id_from_registered_name(dog_line[i])
                dog.living_status = "alive"
            elif i == 1:
                if dog_line[i].lower() == "m":
                    dog.gender = "M"
                else:
                    dog.gender = "F"
            elif i == 2:
                if dog_line[i] != '':
                    parent1_id = id_from_registered_name(dog_line[i])
                    parent1_dog = db.first_or_404(sa.select(Dog).where(Dog.id == parent1_id))
                    dog.set_child_of(parent1_dog)
            elif i == 3:
                if dog_line[i] != '':
                    parent2_id = id_from_registered_name(dog_line[i])
                    parent2_dog = db.first_or_404(sa.select(Dog).where(Dog.id == parent2_id))
                    dog.set_child_of(parent2_dog)
            elif i == 4:
                dog = set_dog_attr(dog, "dilated_cardiomyopathy", dog_line[i])
            elif i == 5:
                dog = set_dog_attr(dog, "cardiomyopathy", dog_line[i])
            elif i == 6:
                dog = set_dog_attr(dog, "progressive_retinal_atrophy", dog_line[i])
            elif i == 7:
                dog = set_dog_attr(dog, "retinal_dysplasia", dog_line[i])
            elif i == 8:
                dog = set_dog_attr(dog, "chondrodystrophy", dog_line[i])
            elif i == 9:
                dog = set_dog_attr(dog, "muscular_dystrophy", dog_line[i])
            elif i == 10:
                dog = set_dog_attr(dog, "myotonia_congenita", dog_line[i])
            elif i == 11:
                dog = set_dog_attr(dog, "degenerative_myelopathy", dog_line[i])
            elif i == 12:
                dog = set_dog_attr(dog, "ichthyosis", dog_line[i])
            elif i == 13:
                dog = set_dog_attr(dog, "primary_glomerulopathy", dog_line[i])
            elif i == 14:
                dog = set_dog_attr(dog, "urolithiasis", dog_line[i])
            # begin phenotypes
            elif i == 15:
                dog = set_dog_attr(dog, "endocardiosis", dog_line[i])
            elif i == 16:
                dog = set_dog_attr(dog, "chiari_malformation", dog_line[i])
            elif i == 17:
                dog = set_dog_attr(dog, "deafness_congenital", dog_line[i])
            elif i == 18:
                dog = set_dog_attr(dog, "mitral_valve_dysplasia", dog_line[i])
            elif i == 19:
                dog = set_dog_attr(dog, "patent_ductus_arteriosus", dog_line[i])
            elif i == 20:
                dog = set_dog_attr(dog, "pulmonic_stenosis", dog_line[i])
            elif i == 21:
                dog = set_dog_attr(dog, "ventricular_septal_defect", dog_line[i])
            elif i == 22:
                dog = set_dog_attr(dog, "corneal_dystrophy", dog_line[i])
            elif i == 23:
                dog = set_dog_attr(dog, "distichiasis", dog_line[i])
            elif i == 24:
                dog = set_dog_attr(dog, "keratoconjunctivitis_sicca", dog_line[i])
            elif i == 25:
                dog = set_dog_attr(dog, "exocrine_pancreatic_insufficiency", dog_line[i])
            elif i == 26:
                dog = set_dog_attr(dog, "cervical_spondylomyelopathy", dog_line[i])
            elif i == 27:
                dog = set_dog_attr(dog, "elbow_dysplasia", dog_line[i])
            elif i == 28:
                dog = set_dog_attr(dog, "hip_dysplasia", dog_line[i])
            elif i == 29:
                dog = set_dog_attr(dog, "patellar_luxation", dog_line[i])
            elif i == 30:
                dog = set_dog_attr(dog, "epilepsy", dog_line[i])
            elif i == 31:
                dog = set_dog_attr(dog, "atopy", dog_line[i])
            elif i == 32:
                dog = set_dog_attr(dog, "umbilical_hernia", dog_line[i])
            elif i == 33:
                dog = set_dog_attr(dog, "addisons_disease", dog_line[i])
            elif i == 34:
                dog = set_dog_attr(dog, "autoimmune_thyroid_disease", dog_line[i])
            elif i == 35:
                dog = set_dog_attr(dog, "diabetes_mellitus", dog_line[i])
            elif i == 36:
                dog = set_dog_attr(dog, "entropion", dog_line[i])
            elif i == 37:
                dog = set_dog_attr(dog, "microphthalmia", dog_line[i])
            elif i == 38:
                dog = set_dog_attr(dog, "persistent_pupillary_membranes", dog_line[i])
            elif i == 39:
                dog = set_dog_attr(dog, "vitreous_degeneration", dog_line[i])
            elif i == 40:
                dog = set_dog_attr(dog, "protein_losing_enteropathy", dog_line[i])
            elif i == 41:
                dog = set_dog_attr(dog, "legg_calve_perthes_disease", dog_line[i])
            elif i == 42:
                dog = set_dog_attr(dog, "hydrocephalus", dog_line[i])
            elif i == 43:
                dog = set_dog_attr(dog, "cleft_palate", dog_line[i])
            elif i == 44:
                dog = set_dog_attr(dog, "demodicosis", dog_line[i])
            elif i == 45:
                dog = set_dog_attr(dog, "cryptorchidism", dog_line[i])
            elif i == 46:
                dog = set_dog_attr(dog, "chronic_hepatitis", dog_line[i])
        db.session.commit()
        del dog

def parse_conformation_from_html(html_data, dog):

    soup = BeautifulSoup(html_data, 'html.parser')

    conformation_info = soup.find("h3", string="Conformation Traits").parent.next_sibling
    trait_list = ["Muzzle Length", "Muzzle Depth","Dewlap","Brow Ridge", "Profile", "Bite", "Skull", "Head Width", "Stop", "Head Carriage", "Ear Ser", "Ear Length", "Ear Width", "Ear Points", "Ear Carriage", "Eye Size", "Eye Shape", "Bone", "Build", "Back Length", "Back Shape", "Topline", "Neck Length", "Croup", "Chest Depth", "Chest Width", "Tuck", "Wrinkle", "Leg Length", "Front Angulation", "Rear Angulation", "Reach", "Drive", "Pasterns", "Feet", "Hind Dew Claws", "Tail Shape", "Tail Length", "Tail Set", "Tail Carriage", "Hairless", "Coat Length", "Furnishings", "Topknot", "Ear Fringe Type", "Ear Fringe Length", "Neck Ruff", "Body Coat", "Leg Feather", "Tail Plume", "Coat Curl", "Texture", "Undercoat", "Coat Lay", "Ridge", "Shedding", "Coat Type Genotype", "Eye Colour", "Pigment", "Nose Colour", "Coat Colour Genotype", "Coat Colour"]
    for element in conformation_info:
        if len(element.find_all("div")) > 0:
            trait_status_string = element.find_all("div")[-1].text
            for trait in trait_list:
                if trait in trait_status_string:
                    setattr(dog, trait.replace(" ", "_").lower(), trait_status_string[len(trait):])
    setattr(dog, "conformation_score", 5)
    return dog

def parse_health_from_html(html_data, dog):

    soup = BeautifulSoup(html_data, 'html.parser')

    disease_info = soup.find("h3", string="Genetic Diseases").parent.next_sibling

    for element in disease_info:
        if "Genotype Affected Carrying Clear" in element.text:
            disease_status_string = element.find_all("div")[-1].text
            status_index = disease_status_string.index("Genotype Affected Carrying Clear")
            setattr(dog, disease_status_string[0:status_index].replace(" ", "_").lower(), "Genotype Affected Carrying Clear")
        elif "Genotype Affected" in element.text:
            disease_status_string = element.find_all("div")[-1].text
            status_index = disease_status_string.index("Genotype Affected")
            setattr(dog, disease_status_string[0:status_index].replace(" ", "_").lower(), "Genotype Affected")
        elif "Genotype Carrier" in element.text:
            disease_status_string = element.find_all("div")[-1].text
            status_index = disease_status_string.index("Genotype Carrier")
            setattr(dog, disease_status_string[0:status_index].replace(" ", "_").lower(), "Genotype Carrier")
        elif "Genotype Clear" in element.text:
            disease_status_string = element.find_all("div")[-1].text
            status_index = disease_status_string.index("Genotype Clear")
            setattr(dog, disease_status_string[0:status_index].replace(" ", "_").lower(), "Genotype Clear")
        elif "Phenotype Clear" in element.text:
            disease_status_string = element.find_all("div")[-1].text
            status_index = disease_status_string.index("Phenotype Clear")
            setattr(dog, disease_status_string[0:status_index].replace(" ", "_").lower(), "Phenotype Clear")
        elif "Phenotype Affected" in element.text:
            disease_status_string = element.find_all("div")[-1].text
            status_index = disease_status_string.index("Phenotype Affected")
            setattr(dog, disease_status_string[0:status_index].replace(" ", "_").lower(), "Phenotype Affected")
    setattr(dog, "health_score", 5)
    return dog

def registered_name_from_id(dog_id):
    dog_id_string = str(dog_id)
    registered_name_string = ""
    count = 0
    for letter in dog_id_string:
        if count == 3:
            registered_name_string = registered_name_string + " "
        if letter == "1":
            registered_name_string = registered_name_string + "q"
        elif letter == "2":
            registered_name_string = registered_name_string + "w"
        elif letter == "3":
            registered_name_string = registered_name_string + "e"
        elif letter == "4":
            registered_name_string = registered_name_string + "r"
        elif letter == "5":
            registered_name_string = registered_name_string + "t"
        elif letter == "6":
            registered_name_string = registered_name_string + "y"
        elif letter == "7":
            registered_name_string = registered_name_string + "u"
        elif letter == "8":
            registered_name_string = registered_name_string + "i"
        elif letter == "9":
            registered_name_string = registered_name_string + "o"
        elif letter == "0":
            registered_name_string = registered_name_string + "p"
        count = count + 1
    return registered_name_string

def create_descendant_disease_dict(dog, generation_index, descendant_disease_dict):
    print("start function:" + str(dog.id) + " " + str(generation_index))
    pprint(descendant_disease_dict)
    children = dog.list_children()
    next_generation_index = generation_index + 1
    for child in children:
        print("call function:" + str(child.id) + " " + str(next_generation_index))
        descendant_disease_dict = create_descendant_disease_dict(child, next_generation_index,
                                                                               descendant_disease_dict)
    # add existance check
    if generation_index in descendant_disease_dict:
        health_dict = descendant_disease_dict[generation_index]
    else:
        health_dict = {}
        descendant_disease_dict[generation_index] =health_dict

    affected_health_values = ["Phenotype Affected", "Genotype Carrier", "Genotype Affected",
                              "Genotype Affected Carrying Clear"]

    for attr, value in dog.__dict__.items():
        if value is not None or value != "None" or str(type(value)) != "<class 'NoneType'>":
            if value in affected_health_values:
                if attr in health_dict:
                    health_dict[attr] = health_dict[attr] + 1
                else:
                    health_dict[attr] = 1
        else:
            print("None")
    descendant_disease_dict[generation_index] = health_dict
    print("end function:" + str(dog.id) + " " + str(generation_index))
    pprint(descendant_disease_dict)
    return descendant_disease_dict
