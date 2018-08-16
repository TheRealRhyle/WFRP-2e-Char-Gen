# import pickle
#
# char = {
#     'starsign': 'The Drummer - Sign of Excess and Hedonism',
#     'skills': ['Common Knowledge (Elves)', 'Speak Language (Eltharin)', 'Speak Language (Reikspiel)'],
#     'talents': ['Aethyric Attunement or Specialist Weapon Group (Longbow)', 'Coolheaded or Savvy', 'Excellent Vision',
#                 'Night Vision'],
#     'main_profile_header': 'WS\tBS\tS\tT\tAg\tInt\tWP\tFel\t',
#     'main_profile': '35\t40\t35\t31\t41\t29\t24\t39\t',
#     'main_profile_adv': '5\t5\t0\t0\t10\t10\t5\t0',
#     'secondary_profile_header': 'A\tW\tSB\tTB\tM\tMag\tIP\tFP\t',
#     'secondary_profile': '1\t11\t3\t3\t5\t0\t0\t2\t',
#     'secondary_profile_adv': '2\t0\t0\t0\t0\t0\t0\t0',
#     'adv_skill': ['Concealment', 'Dodge Blow', 'Follow Trail', 'Heal or Search', 'Outdoor Survival', 'Perception',
#                   'Scale SheerSurface', 'Silent Move'],
#     'adv_talent': ['Marksman or Rover', 'Rapid Reload or Warrior Born'],
#     'trappings': ['Elfbow with 10 arrows', 'Light Armour (Leather Jack)'],
#     'career_entries': ['Hunter', 'Messenger'],
#     'career_exits': ['Hunter', 'Outrider', 'Vagabond', 'Veteran']
# }
#
# skill = 0
# while skill < len(char['talents']):
#     if ' or ' in char['talents'][skill]:
#         print(char['talents'][skill])
#         selection = input('A selection must be made: ' + char['talents'][skill] + ": ")
#         char['talents'].remove(char['talents'][skill])
#         char['talents'].append(selection)
#         skill -= 1
#     skill += 1
#
# print(sorted(char['talents']))
#
#
# # for skill in range(len(sorted(char['talents']))):
# #     print(char['talents'][skill])
# #     if ' or ' in char['talents'][skill]:
# #         selection = input('A selection must be made: ' + char['talents'][skill])
# #         char['talents'].remove(char['talents'][skill])
# #         char['talents'].append(selection)
# #         print(char['talents'])

