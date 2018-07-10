import random
from random import randint
import time
import sys


class Character:
    def __init__(self, first, last):
        self.first = first
        self.last = last


def slowprint(string):
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.randint(1, 2))

    print(end='\n\n')


def to_be_implemented():
    random_char = str(input("Random character: [Y/n] ") or "Y")

    print('Creating a random character, please wait', end="")
    slowprint('. . .')
    print('Done')
    print('Press any key to end.')
    input()


def profiles():
    dwarf_main_profile = [30, 20, 20, 30, 10, 20, 20, 10]
    dwarf_secondary_profile = [1, 0, 0, 0, 3, 0, 0, 0]

    elf_main_profile = [20, 30, 20, 20, 30, 20, 20, 20]
    elf_secondary_profile = [1, 0, 0, 0, 5, 0, 0, 0]

    halfling_main_profile = [10, 30, 10, 10, 30, 20, 20, 30]
    halfling_secondary_profile = [1, 0, 0, 0, 4, 0, 0, 0]

    human_main_profile = [20, 20, 20, 20, 20, 20, 20, 20]
    human_secondary_profile = [1, 0, 0, 0, 4, 0, 0, 0]
