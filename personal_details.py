from random import randint
race = 'dwarf'


def height(race, gender):
    if race == 'dwarf':
        height = 50
    elif race == 'elf':
        height = 64
    elif race == 'halfling':
        height = 38
    elif race == 'human':
        height = 61

    if gender == 'male':
        height = height + 2

    height = height + randint(1, 10)

    height = str(int(height / 12)) + "'" + str(int(height % 12)) + '"'

    return(height)


def weight(race):
    if race == 'dwarf':
        race_base_weight = 90
    if race == 'elf':
        race_base_weight = 90
    if race == 'halfling':
        race_base_weight = 90
    if race == 'human':
        race_base_weight = 90

    weight_selection = randint(1, 20)
    weight_list = [(race_base_weight + i) for i in range(1, 100) if i % 5 == 0]
    weight_list.insert(0, race_base_weight)
    weight = weight_list[weight_selection - 1]

    return weight


def hair_color(race):
    rand_hc = randint(0, 10)
    if race == 'dwarf':
        hair_color = ['Ash-blond', 'Yellow', 'Red', 'Copper', 'Light Brown', 'Brown', 'Brown', 'Dark Brown', 'Blue-black', 'Black']
    elif race == 'elf':
        hair_color = ['Silver', 'Ash-blond', 'Corn', 'Yellow', 'Copper', 'Light Brown', 'Light Brown', 'Brown', 'Dark Brown', 'Black']
    elif race == 'halfling':
        hair_color = ['Ash-blond', 'Corn', 'Yellow', 'Yellow', 'Copper', 'Red', 'Light Brown', 'Brown', 'Dark Brown', 'Black']
    elif race == 'human':
        hair_color = ['Ash-blond', 'Corn', 'Yellow', 'Copper', 'Red', 'Light Brown', 'Brown', 'Brown', 'Dark Brown', 'Black']
    else:
        hair_color = ['Bald', 'Bald', 'Bald', 'Bald', 'Bald', 'Bald', 'Bald', 'Bald', 'Bald', 'Bald']

    hc = hair_color[rand_hc - 1]
    return hc


def eye_color(race):
    rand_ec = randint(0, 10)
    if race == 'dwarf':
        eye_color = ['Pale Grey', 'Blue', 'Copper', 'Light Brown', 'Light Brown', 'Brown', 'Brown', 'Dark Brown', 'Dark Brown', 'Purple']
    elif race == 'elf':
        eye_color = ['Grey-blue', 'Blue', 'Green', 'Copper', 'Light Brown', 'Brown', 'Dark Brown', 'Silver', 'Purple', 'Black']
    elif race == 'halfling':
        eye_color = ['Blue', 'Hazel', 'Hazel', 'Light Brown', 'Light Brown', 'Brown', 'Brown', 'Dark Brown', 'Dark Brown', 'Dark Brown']
    elif race == 'human':
        eye_color = ['Pale Grey', 'Grey-blue', 'Blue', 'Green', 'Copper', 'Light Brown', 'Brown', 'Dark Brown', 'Purple', 'Black']
    else:
        eye_color = ['Bald', 'Bald', 'Bald', 'Bald', 'Bald', 'Bald', 'Bald', 'Bald', 'Bald', 'Bald']

    ec = eye_color[rand_ec - 1]
    return ec


def distinctive_marks():
    distinctive_marks = ['Pox Marks', 'Ruddy Faced', 'Scar', 'Tattoo', 'Earring', 'Ragged Ear', 'Nose Ring', 'Wart', 'Broken Nose', 'Missing tooth', 'Snaggle Teeth', 'Lazy Eye', 'Missing Eyebrow(s)', 'Missing digit', 'Missing Nail', 'Distinctive Gait', 'Curious Smell', 'Huge Nose', 'Large Mole', 'Small Bald Patch', 'Strange Colord Eye(s)']
    rand_dm = randint(0, len(distinctive_marks) - 1)
    dm = distinctive_marks[rand_dm]
    return dm


# sc = personal_details.starting_career(race)
'''
h = personal_details.height(race)
w = personal_details.weight(race)

ec = personal_details.eye_color(race)
dm = personal_details.distinguishing_marks(race)
sib = personal_details.siblings(race)
ss = personal_details.star_sign(race)
age = personal_details.age(race)
bp = personal_details.birthplace(race)
nam = personal_details.names(race)
'''
