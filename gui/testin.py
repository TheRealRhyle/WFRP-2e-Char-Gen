import re
blob = '''Skills: Animal Care, Drive, Gossip or Haggle, Heal or Ride,
Navigation, Perception, Secret Signs (Ranger), Speak
Language (Breton, Kislevian, or Tilean).
Talents: Quick Draw or Seasoned Traveller, Specialist
Weapon Group (Gunpowder).
Trappings: Blunderbuss with powder/ammunition enough
for 10 shots, Medium Armour (Mail Shirt and Leather
Jack), Instrument (Coach Horn).
Career Entries: Outrider, Messenger.
Career Exits: Ferryman, Highwayman, Outlaw, Roadwarden,
Scout, Smuggler, Toll Keeper.'''

blob = blob.replace('\n','').replace('.','\n')
breakdown = re.split('; |: |\*|\n',blob)

skills = f'{breakdown[0]}: {breakdown[1]}'
skills = re.sub(r',\b',', ', skills)

talents = f'{breakdown[2]}: {breakdown[3]}'
talents = re.sub(r',\b',', ', talents)

trappings = f'{breakdown[4]}: {breakdown[5]}'
trappings = re.sub(r',\b',', ', trappings)

print(skills + '\n' + talents +'\n'+ trappings)

# for i in range(len(breakdown)):
#     print(breakdown[i])
