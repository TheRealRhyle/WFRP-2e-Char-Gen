# WFRP Character generator
# Created as a personal project
import pickle
import random
import re
import careers
import personal_details as pd
import races
import skills
import career_listf as cl

race = ['dwarf', 'elf', 'halfling', 'human']
gender = ('male', 'female')

def build_random_char():
    rand_race = race[random.randint(0, 3)]
    rand_gender = gender[random.randint(0, 1)]

    # Get starting Skills and Talents based on rand_race
    ski, tal = skills.skills_talents(rand_race)

    ski = sorted(ski)
    tal = sorted(tal)

    ski = select_option(ski)
    tal = select_option(tal)

    mp_key, mp_value, sp_key, sp_value = random_stat_blocks(rand_race, tal)

    # Select random career
    sel_career_name = careers.starting_career(rand_race)

    #get career info for selected career
    sel_career = cl.career_selection(sel_career_name + ' Advance Scheme')
    mp_adv = list(sel_career['Statblock'])[0:8]
    sec_adv = list(sel_career['Statblock'])[8:]
    mp_adv = '\t'.join(str(li) for li in mp_adv)
    sec_adv = '\t'.join(str(li) for li in sec_adv)
    adv_skill = sorted(sel_career['Skills'])
    adv_talent = sorted(sel_career['Talents'])
    trappings = sorted(sel_career['Trappings'])
    career_entries =sel_career['Career Entries']
    career_exits =sel_career['Career Exits']

    trappings = select_option(trappings)

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
    charout['adv_skill'] = adv_skill
    charout['adv_talent'] = adv_talent
    charout['trappings'] = trappings
    charout['career_entries'] = career_entries
    charout['career_exits'] = career_exits
    return charout

def perm_talen_adj(tal, mp_value, sp_value):
    # Test for perm stat adjustments
    perm_adjust_talents = {'Coolheaded': ('WP', 5), 'Fleet Footed': ('M', 1), 'Hardy': ('W', 1),
                           'Lightning Reflexes': ('Ag', 5), 'Marksman': ('BS', 5), 'Savvy': ('Int', 5),
                           'Suave': ('Fel', 5), 'Very Resilient': ('T', 5), 'Very Strong': ('S', 5),
                           'Warrior Born': ('WS', 5)}

    tal_count = 0
    while tal_count < len(tal):
        # for x in range(len(tal)-1):
        if tal[tal_count] in perm_adjust_talents:
            talent_adj = perm_adjust_talents[tal[tal_count]]

            if talent_adj[0] in mp_value.keys():
                mp_value[talent_adj[0]] = mp_value[talent_adj[0]] + talent_adj[1]
            elif talent_adj[0] in sp_value.keys():
                sp_value[talent_adj[0]] = sp_value[talent_adj[0]] + talent_adj[1]

        tal_count += 1
    return mp_value, sp_value

def random_stat_blocks(race, tal):
    # Generate Main and Secondary Profiles
    mp, sp = races.profiles(race)
    str_bonus, tough_bonus = '', ''

    perm_talen_adj(tal, mp, sp)

    mp_key, mp_value = '', ''
    for key, value in mp.items():
        mp_key = mp_key + key + '\t'

    for key, value in mp.items():
        if key == 'S':
            str_bonus = int(value/10)
        if key == 'T':
            tough_bonus = int(value/10)
        mp_value = str(mp_value) + str(value) + '\t'

    sp_key, sp_value = '', ''
    for key, value in sp.items():
        sp_key = sp_key + key + '\t'

    for key, value in sp.items():
        if key == 'SB':
            value = str_bonus
        if key == 'TB':
            value = tough_bonus
        sp_value = str(sp_value) + str(value) + '\t'



    return (mp_key, mp_value, sp_key, sp_value)

def select_option(stt_selection):
    options = 0
    while options < len(stt_selection):
        if ' or ' in stt_selection[options]:
            selection = input('You must choose between ' + stt_selection[options] + ": ")
            stt_selection.remove(stt_selection[options])
            stt_selection.append(selection)
            options -= 1
        options += 1
    return stt_selection

def save_character(charout):
    with open('characters\{}.dat'.format(charout['name']), 'wb') as f:
        pickle.dump(charout, f)

def load_character(char):
    with open('characters\{}.dat'.format(char), 'rb') as f:
        charin = pickle.load(f)
    return charin

def format_sheet(charin):
    charin['weight'] = str(charin['weight'])

    # skills = charin['skills']
    skills = ', '.join(sorted(charin['skills']))
    talents = ', '.join(sorted(charin['talents']))
    adv_skill = ', '.join(sorted(charin['adv_skill']))
    adv_talent = ', '.join(sorted(charin['adv_talent']))
    trappings = ', '.join(sorted(charin['trappings']))
    career_entries = ', '.join(sorted(charin['career_entries']))
    career_exits = ', '.join(sorted(charin['career_exits']))

    sheet = """Name: {name} the {career}
    Race: {race} Gender: {gender} Age: {age}
    Height: {height} Hair Color: {hair_color} Siblings: {siblings}
    Weight: {weight} Eye Color: {eye_color}
    Birthplace: {birthplace}
    Star Sign: {starsign}
    Distinguishing Marks: {marks}
    
    Main Profile:\t{main_profile_header}
    Main Profile:\t{main_profile}
    Main Advance:\t{main_profile_adv}
    Advance Taken: [  ][  ][  ][  ][  ][  ][  ][  ]
        
    Sec Profile:\t{secondary_profile_header}
    Sec Profile:\t{secondary_profile}
    Sec Advance:\t{secondary_profile_adv}
    Advance Taken: [  ][  ][  ][  ][  ][  ][  ][  ]
        
    Trappings:
    -------
    {}
    
    Skills:
    -------
    {}
       
    Talents:
    -------
    {}
    
    Skill Advancements:
    -------
    {}
    
    Talent Advancements:
    -------
    {}
    
    Career Entries
    -------
    {}
    
    Career Exits
    -------
    {}
    
    """.format(trappings, skills, talents, adv_skill, adv_talent, career_entries,career_exits, **charin).replace('    ','')

    sheet_as_html = sheet.replace('\n','<br>')
    header = '<html><title>{name}</title><body>'.format(**charin)
    with open('characters\{name}.html'.format(**charin),'w+') as file:
        file.write(header)
        file.write(sheet_as_html)
        file.write('</body></html>')
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
        elif ser.lower() == 'e':
            print('Now exiting.')
        else:
            ser = input('[S]ave,[E]xit,[R]eroll: ')
            mainloop(ser)

    elif option.lower() == 'l':
        char = input('Character name: ')
        lc = load_character(char)
        print(format_sheet(lc))
    else:
        print('Not a valid selection, please try again.')
        option = input('Would you like to [G]enerate a Random Character or [L]oad a character?')
        mainloop(option)

if __name__=='__main__':
    option = input('Would you like to [G]enerate a Random Character or [L]oad a character?')
    print('')
    mainloop(option)
