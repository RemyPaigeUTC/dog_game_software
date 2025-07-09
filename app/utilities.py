from bs4 import BeautifulSoup

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

def parse():
    print("nothing")

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