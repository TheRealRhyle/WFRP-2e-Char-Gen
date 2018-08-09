from random import randint


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

    ec = eye_color[rand_ec - 1]
    return ec


def distinctive_marks():
    distinctive_marks = ['Pox Marks', 'Ruddy Faced', 'Scar', 'Tattoo', 'Earring', 'Ragged Ear', 'Nose Ring', 'Wart', 'Broken Nose', 'Missing tooth', 'Snaggle Teeth', 'Lazy Eye', 'Missing Eyebrow(s)', 'Missing digit', 'Missing Nail', 'Distinctive Gait', 'Curious Smell', 'Huge Nose', 'Large Mole', 'Small Bald Patch', 'Strange Colord Eye(s)']
    rand_dm = randint(0, len(distinctive_marks) - 1)
    dm = distinctive_marks[rand_dm]
    return dm


def number_siblings(race):
    sibling_roll = randint(0, 5)
    dict_siblings = {
        'dwarf': [0, 0, 1, 1, 2, 3],
        'elf': [0, 1, 1, 2, 2, 3],
        'halfling': [1, 2, 3, 4, 5, 6],
        'human': [0, 1, 2, 3, 4, 5]
    }
    sib = dict_siblings[race][sibling_roll]
    return sib


def age(race):
    age_roll = randint(0, 19)
    base_age_dh = 20
    base_age_e = 30
    base_age_hu = 16
    dict_age = {
        'dwarf': [(base_age_dh + i) for i in range(0, 100) if i % 5 == 0],
        'elf': [(base_age_e + i) for i in range(0, 100) if i % 5 == 0],
        'halfling': [(base_age_dh + i) for i in range(0, 41) if i % 2 == 0],
        'human': [(base_age_hu + i) for i in range(0, 20)]

        # weight_list = [(race_base_weight + i) for i in range(1, 100) if i % 5 == 0]
    }
    age_list = dict_age[race]
    _age = age_list[age_roll]
    return _age


def birthplace(race):
    dict_sl = {
        'human': [['Averland', 'Hochland', 'Middenland', 'Nordland', 'Ostermark', 'Ostland', 'Reikland', 'Stirland', 'Talabecland', 'Wissenland'], ['City', 'Prosperous Town', 'Market Town', 'Fortified Town', 'Farming Village', 'Poor Village', 'Small Settlement', 'Pig/Cattle Farm', 'Arable Farm', 'Hovel']],
        'dwarf': ['Roll on Human', 'Karak Norn (Grey Mountains)', 'Karak Izor (the Vaults)', 'Karak Hirn (Black Mountains)', 'Karak Kadrin (World\'s Edge Mountians)', 'Karaz-a-Karak (World\'s Edge Mountians)', 'Zhufbar (World\'s Edge Mountians)', 'Barak Varr (the Black Gulf)'],
        'elf': ['City of Altdorf', 'City of Marienburg', 'Laurelorn Forest', 'The Great Forest', 'Reikwald Forest'],
        'halfling': ['The Moot', 'Roll on Human']
    }

    hl_roll = randint(0, len(dict_sl[race]) - 1)

    if race == 'human' or dict_sl[race][hl_roll] == 'Roll on Human':
        region = randint(0, len(dict_sl['human'][0]) - 1)
        pop = randint(0, len(dict_sl['human'][1]) - 1)
        if str(dict_sl['human'][1][pop])[0] == 'A':
            sl = str('An ' + str(dict_sl['human'][1][pop]) + ' in the province of ' + str(dict_sl['human'][0][region]))
        else:
            sl = str('A ' + str(dict_sl['human'][1][pop]) + ' in the province of ' + str(dict_sl['human'][0][region]))
    else:
        sl = dict_sl[race][hl_roll]

    return sl


def get_names(race, gender):
    dict_names = {
        'dwarf': [['Anika', 'Asta', 'Astrid', 'Berta', 'Birgit', 'Dagmar', 'Elsa', 'Erika', 'Franziska', 'Greta', 'Hunni', 'Ingrid', 'Janna', 'Karin', 'Petra', 'Sigrid', 'Sigrun', 'Silma', 'Thylda', 'Ulla'], ['Bardin', 'Brokk', 'Dimzad', 'Durak', 'Garil', 'Gottri', 'Grundi', 'Hargin', 'Imrak', 'Kargun', 'Jotunn', 'Magnar', 'Mordrin', 'Nargond', 'Orzad', 'Ragnar', 'Snorri', 'Storri', 'Thingrim', 'Urgrim']],
        'elf': [['Alane', 'Altronia', 'Davandrel', 'Eldril', 'Eponia', 'Fanriel', 'Gallina', 'Halion', 'Iludil', 'Ionor', 'Lindara', 'Lorandara', 'Maruviel', 'Pelgrana', 'Siluvaine', 'Tallana', 'Ulliana', 'Vivandrel', 'Yuviel'], ['Aluthol', 'Amendil', 'Angran', 'Cavindel', 'Dolwen', 'Eldillor', 'Falandar', 'Farnoth', 'Gildiril', 'Harrond', 'Imhol', 'Larandar', 'Laurenor', 'Mellion', 'Mormacar', 'Ravandil', 'Torendil', 'Yavandir']],
        'halfling': [['Agnes', 'Alice', 'Elena', 'Eva', 'Frida', 'Greta', 'Hanna', 'Heidi', 'Hilda', 'Janna', 'Karin', 'Lendi', 'Marie', 'Petra', 'Silma', 'Sophia', 'Susi', 'Theda', 'Ulla', 'Wanda'], ['Adam', 'Albert', 'Alfred', 'Axel', 'Carl', 'Edgar', 'Hugo', 'Jakob', 'Ludo', 'Max', 'Nuiklaus', 'Oskar', 'Paul', 'Ralf', 'Rudi', 'heo', 'Thomas', 'Udo', 'Viktor', 'Walter', ]],
        'human': [['Alexa', 'Alfrida', 'Beatrix', 'Bianka', 'Carlott', 'Elfrida', 'Elise', 'Gabrielle', 'Gretchen', 'Hanna', 'Ilsa', 'Klara', 'Jarla', 'Ludmilla', 'Mathilde', 'Regina', 'Solveig', 'Theodora', 'Ulrike', 'Wertha'], ['Adelbert', 'Albrecht', 'Berthold', 'Dieter', 'Eckhardt', 'Felix', 'Gottfried', 'Gustav', 'Heinz', 'Johann', 'Konrad', 'Leopold', 'Magnus', 'Otto', 'Pieter', 'Rudiger', 'Siegfried', 'Ulrich', 'Waldenmar', 'Wolfgang']]
    }

    first_name_list = []
    last_name_list = []

    if gender == 'male':
        first_name_list = dict_names[race][1]
        last_name_list = dict_names[race][1]
    if gender == 'female':
        first_name_list = dict_names[race][0]
        last_name_list = dict_names[race][1]

    first_name_roll = randint(0, len(first_name_list) - 1)
    last_name_roll = randint(0, len(last_name_list) - 1)

    char_name = (first_name_list[first_name_roll] + ' ' + last_name_list[last_name_roll])
    return char_name


def star_sign():
    ssign = ['Wymund the Anchorite - Sign of Enduring','The Big Cross - Sign of Clarity','The Limner\'s line - Sign of Percision','Gnuthus the Ox - Sign of Dutiful Service','Dragonmas the Drake - Sign of Courage','The Gloaming - Sign of Illusion and Mastery','Grungi\'s Baldric - Sign of Martial Pursuits','Mammit the Wise - Sign of Wisdom','Mummit the Fool - Sign of Instinct','The Two Bullocks - Sign of Fertility and Craftsmanship','The Dancer - Sign of Love and Attraction','The Drummer - Sign of Excess and Hedonism','The Piper - Sign of the Trickster','Vobist the Faint - Sign of Darkness and Uncertainty','The Broken Cart - Sign of Pride','The Greased Goat - Sign of Denied Passions','Rhya\'s Cauldron - Sign of Mercy, Death and Creation','Cackelfax the Cockerel - Sign of Money and Merchants','The Bonesaw - Sign of Skill and Learning','The Witching Star - Sign of Magic']
    random_ssign = randint(0, len(ssign)-1)

    return ssign[random_ssign]

#if __name__  = __main__():
