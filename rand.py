from random import randint

starting_wounds = randint(1, 10)
starting_fate = randint(1, 10)
print(starting_fate)
rce = 'dwarf'

if rce.lower() == 'dwarf':
    main_profile = [30, 20, 20, 30, 10, 20, 20, 10]
    secondary_profile = [1, 0, 0, 0, 3, 0, 0, 0]
    if starting_fate in range(1, 5):
        secondary_profile[7] = 1
    elif starting_fate in range(5, 8):
        secondary_profile[7] = 2
    else:
        secondary_profile[7] = 3

print(main_profile)
print(secondary_profile)
