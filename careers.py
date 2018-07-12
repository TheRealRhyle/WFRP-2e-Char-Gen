from random import randint


def starting_career(race):
    dict_careers = {
        'dwarf': ['Agitator', 'Bodyguard', 'Burgher', 'Coachman', 'Entertainer', 'Jailer', 'Marine', 'Mercenary', 'Militiaman', 'Miner', 'Noble', 'Outlaw', 'Pit Fighter', 'Protagonist', 'Rat Catcher', 'Runebearer', 'Scribe', 'Seaman', 'Servant', 'Shieldbreaker', 'Smuggler', 'Soldier', 'Student', 'Thief', 'Toll Keeper', 'Tomb Robber', 'Tradesman', 'Troll Slayer', 'Watchman'],
        'elf': ['Apprentice Wizard', 'Entertainer', 'Envoy', 'Hunter', 'Kithband Warrior', 'Mercenary', 'Messanger', 'Outlaw', 'Outrider', 'Rogue', 'Scribe', 'Seaman', 'Student', 'Thief', 'Tradesman', 'Vagabond'],
        'halfling': ['Agitator', 'Barber-Surgeon', 'Bone Picker', 'Bounty Hunter', 'Burgher', 'Camp Follower', 'Charcoal-Burner', 'Entertainer', 'Ferryman', 'Fieldwarden', 'Fisherman', 'Grave Tobber', 'Hunter', 'Mercenary', 'Messanger', 'Militiaman', 'Outlaw', 'Peasant', 'Rat Catcher', 'Rogue', 'Servant', 'Smuggler', 'Soldier', 'Student', 'Thief', 'Toll Keeper', 'Tomb Robber', 'Tradesman', 'Vagabond', 'Valet', 'Watchman'],
        'human': ['Agitator', 'Apprentice Wizard', 'Bailiff', 'Barber-Surgeon', 'Boatman', 'Bodyguard', 'Bone Picker', 'Bounty Hunter', 'Burgher', 'Camp Follower', 'Charcoal-Burner', 'Coachman', 'Entertainer', 'Estalian Diestro', 'Ferryman', 'Fisherman', 'Grave Tobber', 'Hedge Wizard', 'Hunter', 'Initiate', 'Jailer', 'Kislevite Kossar', 'Marine', 'Mercenary', 'Messanger', 'Militiaman', 'Miner', 'Noble', 'Norse Erserker', 'Outlaw', 'Outrider', 'Peasant', 'Pit Fighter', 'Protagonist', 'Rat Catcher', 'Roadwarden', 'Rogue', 'Scribe', 'Seaman', 'Servant', 'Smuggler', 'Soldier', 'Squire', 'Student', 'Thief', 'Thug', 'Toll Keeper', 'Tomb Robber', 'Tradesman', 'Vagabond', 'Valet', 'Watchman', 'Woodsman', 'Zealot']
    }

    rand_career = randint(0, len(dict_careers[race]) - 1)
    startingCareer = dict_careers[race][rand_career]

    return startingCareer
