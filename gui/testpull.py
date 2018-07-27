import re
blob = '''— Bone Picker Advance Scheme —
Main Profile
WS BS S T Ag Int WP Fel
+5% — +5% +10% +5% — +5% +5%
Secondary Profile
A W SB TB M Mag IP FP
— +2 — — — — — —
Skills: Animal Care, Charm or Gossip, Drive, Common
Knowledge (the Empire), Evaluate, Haggle, Perception,
Search
Talents: Coolheaded or Streetwise, Hardy or Resistance to
Disease
Trappings: Cart, 3 Sacks
Career Entries: Peasant, Rat Catcher, Vagabond
Career Exits: Camp Follower, Cat Burglar, Fence, Grave
Robber, Smuggler'''

blob = blob.split('\n')
for lns in range(len(blob)):
    if lns == 0:
        continue
    else:
        blob[lns] = blob[lns].replace('—', '0')

for i in range(len(blob)):
    if blob[i][0] == '—':
        blob[i] = blob[i].replace(' —','').replace('— ','')
    if blob[i] == 8:
        
        while blob[8] != 'Talents:':
            blob[7] = blob[7] + blob[7+1]
            del blob[8]

for i in range(len(blob)):
    print(blob[i])
