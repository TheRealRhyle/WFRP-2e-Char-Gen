from random import randint


def skills_talents(rce):
    # Build the Random talent list.
    random_talent_list = ['Acute Hearing', 'Ambidexterous', 'Coolheaded', 'Excellent Vision', 'Fleet Footed', 'Hardy', 'Lightning Reflexes', 'Luck', 'Marksman', 'Mimic', 'Night Vision', 'Resistance to Disease', 'Resistance to Magic', 'Resistance to Poison', 'Savvy', 'Sixth Sense', 'Strong-minded', 'Sturdy', 'Suave', 'Super Numerate', 'Very Resilient', 'Very Strong', 'Warrior Born']

    if rce.lower() == 'dwarf':
        skills = ['Common Knowledge (Dwarfs)', 'Speak language (Khazalid)', 'Speak Language (Reikspiel)', 'Trade (Miner, Smith, or Stonworker)']
        talents = ['Dwarfcraft', 'Grudge-born Fury', 'Night Vision', 'Resistance to Magic', 'Stout-hearted', 'Sturdy']
    elif rce.lower() == 'elf':
        skills = ['Common Knowledge (Elves)', 'Speak Language (Eltharin)', 'Speak Language (Reikspiel)']
        talents = ['Aethyric Arrunement or Specialist Weapon Group (Longbow)', 'Coolheaded or Savvy', 'Excellent Vision', 'Night Vision']
    elif rce.lower() == 'halfling':
        skills = ['Academic Knowledge (Geneology/Heraldry)', 'Common Knowledge (Halflings)', 'Gossip', 'Speak Language (Halfling)', 'Speak Language (Reikspiel)', 'Trade (Cook or Farmer)']
        talents = ['Night Vision', 'Resistance to Chaos', 'Specialist Weapon Group (Sling)']
        # Halflings get one random talent
        _halfling_random_talent = random_talent_list[randint(0, len(random_talent_list) - 1)]
        if _halfling_random_talent == 'Night Vision':
            _halfling_random_talent = random_talent_list[randint(0, len(random_talent_list) - 1)]
        talents.append(_halfling_random_talent)
    elif rce.lower() == 'human':
        skills = ['Common Knowledge (the Empire)', 'Gossip', 'Speak Language (Reikspiel)']
        talents = []
        # Humans get 2 random talents
        for rndTalent in range(0, 2):
            _human_random_talent = random_talent_list[randint(0, len(random_talent_list) - 1)]
            talents.append(_human_random_talent)
    else:
        skills = 'Invalid Race'
        talents = 'Invalid Race'

    return(skills, talents)
