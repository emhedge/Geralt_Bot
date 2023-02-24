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
        return str(random.choice(['Lonely Labs', 'Breakwater Bay', 'Brutal Bastion', 'Faulty Splits', 'Frenzy Fields', 'Shattered Slabs', 'Slappy Shores', 'The Citadel', 'Anvil Square', 'Somewhere cold', 'Somewhere wet', 'A hot zone', 'Somewhere quiet', 'middle of fuckin\' nowhere', 'somewhere gay for John']))
    # not finished if p_message == 'Tell me something interesting':
        # need to figure it out return str(random.choice[''])
    if p_message == 'berate me':
        return str(random.choice(['f']))
    if p_message == '!help':
        return '`Witchers help those who help themselves.`'




