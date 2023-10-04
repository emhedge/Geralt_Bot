import random


def get_response(message: str) -> str:
   p_message = message.lower()
   if p_message == 'hello':
       return 'Hey there!'
   if message == 'roll':
       return str(random.randint(1, 6))
   if p_message == 'flip':
       return str(random.choice(['Heads', 'Tails']))
   if p_message == 'where to?':
       return str(random.choice(['Lonely Labs', 'Breakwater Bay', 'Brutal Bastion', 'Shady Stilts', 'Frenzy Fields', 'Shattered Slabs', 'Slappy Shores', 'The Citadel', 'Creeky Compound', 'Rumble Ruins', 'Mega City', 'Steamy Springs', 'Kenjutsu Crossing', 'Knotty Nets', 'Somewhere cold', 'Somewhere wet', 'A hot zone', 'Somewhere quiet', 'middle of fuckin\' nowhere', 'somewhere for John']))
   if p_message == 'how?':
       return str(random.choice(['go fish', 'go hard', 'be smart', 'bush it up', 'hide on the edge', 'stay in the middle', 'stick to the cities', 'stick to the stix', 'grenade round', 'snipey snipey']))
   if p_message == 'drg where to?':
       return str(random.choice(['Azure Weald', 'Crystalline Caverns', 'Dense Biozone', 'Fungus Bogs', 'Glacial Strata', 'Hollow Bough', 'Magma Core', 'Radioactive Exclusion Zone', 'Salt Pits', 'Sandblasted Corridors']))
   # not finished if p_message == 'Tell me something interesting':
       # need to figure it out return str(random.choice[''])
   if p_message == 'berate me':
       return str(random.choice(['f']))
   if p_message == '!help':
       return '`Witchers help those who help themselves.`'

