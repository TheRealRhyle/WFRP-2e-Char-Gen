from random import randint
race = ['dwarf', 'elf', 'halfling', 'human']
rand_race = race[randint(0, 3)]
starting_fate = {}
rand_fate = randint(1, 10)

if rand_fate in range(1, 5):
    starting_fate = {'dwarf': 1, 'elf': 1, 'halfling': 2, 'human': 2}
elif rand_fate in range(5, 8):
    starting_fate = {'dwarf': 2, 'elf': 2, 'halfling': 2, 'human': 3}
elif rand_fate in range(8, 11):
    starting_fate = {'dwarf': 3, 'elf': 2, 'halfling': 3, 'human': 3}
else:
    fate = 0

fate = starting_fate[rand_race]
print(rand_race + ' roll ' + str(rand_fate))
print(fate)
