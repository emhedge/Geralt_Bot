import random

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
            return '*grunt*'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return "`If you come to a witcher for help, you're truly fucked.`"

    if p_message == 'flip':
        return str(random.choice(['Heads', 'Tails']))

    if p_message == 'where to?':
        return str(random.choice(['Lonely Labs', 'Breakwater Bay', 'Brutal Bastion', 'Faulty Splits', 'Frenzy Fields', 'Shattered Slabs', 'Slappy Shores', 'The Citadel', 'Anvil Square', 'Somewhere cold', 'Somewhere wet', 'A hot zone', 'Somewhere quiet']))

    if p_message == 'Tell me something interesting':
        return str(random.choice[''])

    return 'huh?'



