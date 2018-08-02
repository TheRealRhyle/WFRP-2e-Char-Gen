# WFRP Character generator
# Created as a personal project
import pickle
import random

import careers
import personal_details as pd
import races
import skills
import career_listf as cl

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

    mp_key, mp_value, sp_key, sp_value = random_stat_blocks(rand_race)

    # Select random career
    sel_career_name = careers.starting_career(rand_race)

    #get career info for selected career
    sel_career = cl.career_selection(sel_career_name + ' Advance Scheme')
    mp_adv = list(sel_career['Statblock'])[0:8]
    sec_adv = list(sel_career['Statblock'])[7:]
    mp_adv = '\t'.join(str(li) for li in mp_adv)
    sec_adv = '\t'.join(str(li) for li in sec_adv)
    #sel_career['Skills'] = '\t'.join(sel_career['Skills'])
    #sel_career['Talents'] = '\t'.join(sel_career['Talents'])

    charout = {}
    charout['name'] = pd.get_names(rand_race, rand_gender)
    charout['career'] = sel_career_name
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
    charout['skills'] = sorted(ski)
    charout['talents'] = sorted(tal)
    charout['main_profile_header'] = mp_key
    charout['main_profile'] = mp_value
    charout['main_profile_adv'] = mp_adv
    charout['secondary_profile_header'] = sp_key
    charout['secondary_profile'] = sp_value
    charout['secondary_profile_adv'] = sec_adv
    charout['adv_skill'] = sel_career['Skills']
    charout['adv_talent'] = sel_career['Talents']
    charout['trappings'] = sel_career['Trappings']

    #charout['starting_stat_block'] = random_stat_blocks(rand_race)

    return charout


def random_stat_blocks(race):
    # Generate Main and Secondary Profiles
    mp, sp = races.profiles(race)

    # Get starting Skills and Talents based on rand_race
    #ski, tal = skills.skills_talents(race)

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

    return (mp_key, mp_value, sp_key, sp_value)

def save_character(charout):
    with open('characters\{}.dat'.format(charout['name']), 'wb') as f:
        pickle.dump(charout, f)

def load_character(char):
    with open('characters\{}.dat'.format(char), 'rb') as f:
        charin = pickle.load(f)

    return format_sheet(charin)

def format_sheet(charin):
    charin['weight'] = str(charin['weight'])

    #skills = charin['skills']
    charin['skills'] = '\n'.join(charin['skills'])
    charin['talents'] = '\n'.join(charin['talents'])
    charin['adv_skill'] = ', '.join(charin['adv_skill'])
    charin['adv_talent'] = ', '.join(charin['adv_talent'])
    charin['trappings'] = ', '.join(charin['trappings'])

    sheet = """Name: {name} the {career}
    Race: {race:15s}Gender: {gender:15s}Age: {age}
    Height: {height:13s}Hair Color: {hair_color:10s}Siblings: {siblings}
    Weight: {weight:13s}Eye Color: {eye_color}
    Birthplace: {birthplace}
    Star Sign: {starsign}
    Distinguishing Marks: {marks}
    
    Main Profile:\t{main_profile_header}
    Main Profile:\t{main_profile}
    Main Advance:\t{main_profile_adv}
    
    Sec Profile:\t{secondary_profile_header}
    Sec Profile:\t{secondary_profile}
    Sec Advance:\t{secondary_profile_adv}
    
    Trappings:
    -------
    {trappings}
    
    Skills:
    -------
    {skills}
       
    Talents:
    -------
    {talents}
    
    Skill Advances:
    -------
    {adv_skill}
    
    Talent Advances:
    -------
    {adv_talent}
    
    """.format(**charin).replace('    ','')

    return sheet

def mainloop(option):
    if option.lower() == 'g':
        charout = build_random_char()
        print(format_sheet(charout))
        ser = input('[S]ave,[E]xit,[R]eroll: ')
        print('')
        if ser.lower() == 's':
            save_character(charout)
            saved=('Character: {} has been saved to characters\{}.dat').format(charout['name'],charout['name'])
            print(saved)
            input('Press [ENTER] key to continue...')
            mainloop('g')
        elif ser.lower() == 'r':
            mainloop('g')
        else:
            print('Have a nice day')

    elif option.lower() == 'l':
        char = input('Character name: ')
        print(load_character(char))
    else:
        print('Not a valid selection, please try again.')

if __name__=='__main__':
    option = input('Would you like to [G]enerate a Random Character or [L]oad a character?')
    print('')
    mainloop(option)
