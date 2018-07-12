import random
from random import randint


def profiles(rce):
    main_profile_dict = {'WS': 0, 'BS': 0, 'S': 0, 'T': 0, 'Ag': 0, 'Int': 0, 'WP': 0, 'Fel': 0}
    secondary_profile_dict = {'A': 0, 'W': 0, 'SB': 0, 'TB': 0, 'M': 0, 'Mag': 0, 'IP': 0, 'FP': 0}
    main_profile = []
    secondary_profile = []

    if rce.lower() == 'dwarf':
        main_profile = [30, 20, 20, 30, 10, 20, 20, 10]
        secondary_profile = [1, 0, 0, 0, 3, 0, 0, 0]

    elif rce.lower() == 'elf':
        main_profile = [20, 30, 20, 20, 30, 20, 20, 20]
        secondary_profile = [1, 0, 0, 0, 5, 0, 0, 0]

    elif rce.lower() == 'halfling':
        main_profile = [10, 30, 10, 10, 30, 20, 20, 30]
        secondary_profile = [1, 0, 0, 0, 4, 0, 0, 0]

    elif rce.lower() == 'human':
        main_profile = [20, 20, 20, 20, 20, 20, 20, 20]
        secondary_profile = [1, 0, 0, 0, 4, 0, 0, 0]

    # Set starting fate points.
    f_roll = randint(0, 2)
    dict_fate = {
        'dwarf': [1, 2, 3],
        'elf': [1, 2, 2],
        'halfling': [2, 2, 3],
        'human': [2, 3, 3]
    }

    # Determine starting Wounds based on Race
    w_roll = randint(0, 3)
    dict_wounds = {
        'dwarf': [11, 12, 13, 14],
        'elf': [9, 10, 11, 12],
        'halfling': [8, 9, 10, 11],
        'human': [10, 11, 12, 13]
    }

    fate = dict_fate[rce][f_roll]
    wound = dict_wounds[rce][w_roll]
    # main_random = [randint(2, 20) for stat in range(len(main_profile))]
    mp = [main_profile[stat] + randint(2, 20) for stat in range(len(main_profile))]

    secondary_profile.insert(7, fate)
    secondary_profile.pop(-1)
    secondary_profile.pop(3)
    secondary_profile.insert(1, wound)

    main_profile = dict(zip(main_profile_dict, mp))
    secondary_profile = dict(zip(secondary_profile_dict, secondary_profile))

    return(main_profile, secondary_profile)
