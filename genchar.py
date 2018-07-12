# WFRP Character generator
# Created as a personal project
import random
import time
import sys
import races
import skills
import personal_details as pd
import careers
from itertools import zip_longest as zl

race = ['dwarf', 'elf', 'halfling', 'human']
gender = ('male', 'female')


class Character:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.skills = skills[]
        # self.talents = talents[]


def slowprint(string):
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(1)

    print(end='\n\n')


def build_random_char():
    # random_char = str(input("Random character: [Y/n] ") or "Y")
    # if random_char == 'Y':

    rand_race = race[random.randint(0, 3)]
    rand_gender = gender[random.randint(0, 1)]
    h = pd.height(rand_race, rand_gender)
    w = pd.weight(rand_race)
    hc = pd.hair_color(rand_race)
    ec = pd.eye_color(rand_race)
    dm = pd.distinctive_marks()
    sib = pd.number_siblings(rand_race)
    _age = pd.age(rand_race)
    sl = pd.birthplace(rand_race)
    character_name = pd.get_names(rand_race, rand_gender)
    sc = careers.starting_career(rand_race)

    # print('Creating a random character, please wait', end="")
    # slowprint('...')

    # Generate Main and Secondary Profiles
    mp, sp = races.profiles(rand_race)

    # Get starting Skills and Talents based on rand_race
    ski, tal = skills.skills_talents(rand_race)

    # Output everything to check
    print('Name: ' + character_name)
    print(rand_race.title() + ' ' + rand_gender.title() + ' the ' + sc)
    print('Height: ' + h + '\tHair Color: ' + hc)
    print('Weight: ' + str(w) + '\t\tEye Color: ' + ec)
    print('Distictive Marks / Features: ' + dm)
    print('Number of siblings: ' + str(sib) + '\tAge: ' + str(_age))
    print('Birthplace: ' + sl)
    print(mp)
    print(str(sp) + '\n')
    print('{:40s} {:40s}'.format('Skills:', 'Talents:'))

    ski = sorted(ski)
    tal = sorted(tal)
    for skill, talent in zl(ski, tal, fillvalue=''):
        print('{:40s} {:40s}'.format(skill, talent))


build_random_char()
