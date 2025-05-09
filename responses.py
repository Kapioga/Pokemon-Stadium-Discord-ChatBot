from random import choice, randint

from poke_requests import pokemon_image


# dice_check :int = 0

def Get_Response(user_input: str) -> str:
    lowered : str = user_input.lower()
    # raise NotImplementedError ("Get Response Implementation Code missing...")

    if lowered == " ":
        return "Hey, Trainer! Are you still there?"
    elif 'pk.hello' in lowered:
        return "Hello, Trainer!"
    elif 'pk.bye' in lowered:
        return "See you, Trainer!"
    elif 'pk.help' in lowered:
        return "What can I do for you, Trainer?"
    elif 'pk.yippee' in lowered:
        return "YIPPEEE!!"
    elif 'pk.how are you' in lowered:
        return choice([
            "Doing alright, thanks for asking!",
            "Never better!",
            "Im doing well!"
        ])
    elif 'pk.pokemon' in lowered:
        dice_check: int = randint(1,1025)
        # return f' You rolled: {dice_check}'
        return pokemon_image(dice_check)
    else:
        return choice([" Could you repeat that? I dont understand....",
                       "What are you talking about?",
                       "Could you rephrase that?",
                       "I dont know what your talking about?"])