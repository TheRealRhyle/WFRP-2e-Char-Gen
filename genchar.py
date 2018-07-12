# WFRP Character generator
# Created as a personal project
import random
import time
import sys
import races
import skills

# combine the
from personal_details import height
from personal_details import weight
from personal_details import hair_color
from personal_details import eye_color
from personal_details import distinctive_marks
from personal_details import number_siblings
from personal_details import age
from personal_details import birthplace
from personal_details import get_names
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
    h = height(rand_race, rand_gender)
    w = weight(rand_race)
    hc = hair_color(rand_race)
    ec = eye_color(rand_race)
    dm = distinctive_marks()
    sib = number_siblings(rand_race)
    _age = age(rand_race)
    sl = birthplace(rand_race)
    character_name = get_names(rand_race, rand_gender)

    # print('Creating a random character, please wait', end="")
    # slowprint('...')

    # Generate Main and Secondary Profiles
    mp, sp = races.profiles(rand_race)

    # Get starting Skills and Talents based on rand_race
    ski, tal = skills.skills_talents(rand_race)

    # Output everything to check
    print('Name: ' + character_name)
    print(rand_race.title() + ' ' + rand_gender.title() + '\n')
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


itr = 0
while itr < 45:
    build_random_char()
    itr += 1
    print('-' * 50)
