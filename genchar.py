# WFRP Character generator
# Created as a personal project
import random
import races
import skills
import personal_details as pd
import careers
import pickle

race = ['dwarf', 'elf', 'halfling', 'human']
gender = ('male', 'female')


class Character:
    def __str__(self):
        pass

    def __init__(self, first, last):
        self.first = first
        self.last = last


def build_random_char():
    rand_race = race[random.randint(0, 3)]
    rand_gender = gender[random.randint(0, 1)]

    # Get starting Skills and Talents based on rand_race
    ski, tal = skills.skills_talents(rand_race)

    ski = sorted(ski)
    tal = sorted(tal)

    charout = {}
    charout['name'] = pd.get_names(rand_race, rand_gender)
    charout['career'] = careers.starting_career(rand_race)
    charout['race'] = rand_race.title()
    charout['gender'] = rand_gender.title()
    charout['height'] = pd.height(rand_race, rand_gender)
    charout['hair_color'] = pd.hair_color(rand_race)
    charout['weight'] = pd.weight(rand_race)
    charout['eye_color'] = pd.eye_color(rand_race)
    charout['marks'] = pd.distinctive_marks()
    charout['age'] = pd.age(rand_race)
    charout['siblings'] = pd.number_siblings(rand_race)
    charout['birthplace'] = pd.birthplace(rand_race)
    charout['starsign'] = pd.star_sign()
    charout['starting_stat_block'] = random_stat_blocks(rand_race)
    charout['skills'] = sorted(ski)
    charout['talents'] = sorted(tal)

    return charout


def random_stat_blocks(race):
    # Generate Main and Secondary Profiles
    mp, sp = races.profiles(race)

    # Get starting Skills and Talents based on rand_race
    ski, tal = skills.skills_talents(race)

    mp_key, mp_value = '', ''
    for key, value in mp.items():
        mp_key = mp_key + key + '\t'

    for key, value in mp.items():
        mp_value = str(mp_value) + str(value) + '\t'

    sp_key, sp_value = '', ''
    for key, value in sp.items():
        sp_key = sp_key + key + '\t'

    for key, value in sp.items():
        sp_value = str(sp_value) + str(value) + '\t'

    main_prof = """\n    ========= Main Profile =========
    {}
    {}

    ====== Secondary Profile =======
    {}
    {}
    """.format(mp_key, mp_value, sp_key, sp_value)

    profile = main_prof  # + '\n' + sec_prof

    return profile


# build_random_char()
# print(random_stat_blocks('dwarf'))

charout = build_random_char()

# with open('{}.dat'.format(charout['name']), 'wb') as f:
#    pickle.dump(charout, f)

with open('Bardin Brokk.dat', 'rb') as f:
    charin = pickle.load(f)

charin['weight'] = str(charin['weight'])

skills = charin['skills']
charin['skills'] = '\n'.join(charin['skills'])
charin['talents'] = '\n'.join(charin['talents'])

sheet = """Name: {name} the {career}
Race: {race:15s}Gender:{gender:15s}Age:{age}
Height: {height:13s}Hair Color: {hair_color:10s}Siblings:{siblings}
Weight: {weight:13s}Eye Color: {eye_color}
Birthplace: {birthplace}
Star Sign: {starsign}
Distinguising Marks: {marks}
{starting_stat_block}
Skills:
-------
{skills:35}

Talents:
-------
{talents}
""".format(ws='', **charin)
