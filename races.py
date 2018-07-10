import random
from random import randint


def profiles(rce):
    main_profile_dict = {'WS': 0, 'BS': 0, 'S': 0, 'T': 0, 'Ag': 0, 'Int': 0, 'WP': 0, 'Fel': 0}
    secondary_profile_dict = {'A': 0, 'W': 0, 'SB': 0, 'TB': 0, 'M': 0, 'Mag': 0, 'IP': 0, 'FP': 0}
    main_profile = []
    secondary_profile = []
    starting_wounds = randint(1, 10)
    starting_fate = randint(1, 10)

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

    # Determine starting Fate points.
    if starting_fate in range(1, 5):
        starting_fate = {'dwarf': 1, 'elf': 1, 'halfling': 2, 'human': 2}
    elif starting_fate in range(5, 8):
        starting_fate = {'dwarf': 2, 'elf': 2, 'halfling': 2, 'human': 3}
    elif starting_fate in range(8, 11):
        starting_fate = {'dwarf': 3, 'elf': 2, 'halfling': 3, 'human': 3}
    else:
        fate = 0

    # Determine starting Wounds based on Race
    if starting_wounds in range(1, 4):
        starting_wounds = {'dwarf': 11, 'elf': 9, 'halfling': 8, 'human': 10}
    elif starting_wounds in range(4, 7):
        starting_wounds = {'dwarf': 12, 'elf': 10, 'halfling': 9, 'human': 11}
    elif starting_wounds in range(7, 10):
        starting_wounds = {'dwarf': 13, 'elf': 11, 'halfling': 10, 'human': 12}
    elif starting_wounds in range(10, 11):
        starting_wounds = {'dwarf': 14, 'elf': 12, 'halfling': 11, 'human': 13}
    else:
        wounds = 0

    fate = starting_fate[rce]
    wound = starting_wounds[rce]
    # main_random = [randint(2, 20) for stat in range(len(main_profile))]
    mp = [main_profile[stat] + randint(2, 20) for stat in range(len(main_profile))]
    sp = secondary_profile.insert(7, fate)
    sp = secondary_profile.insert(1, wound)

    main_profile = dict(zip(main_profile_dict, mp))
    secondary_profile = dict(zip(secondary_profile_dict, secondary_profile))

    return(main_profile, secondary_profile)
