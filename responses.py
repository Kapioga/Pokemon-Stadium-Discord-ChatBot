from random import choice, randint

# dice_check :int = 0

def Get_Response(user_input: str) -> str:
    lowered : str = user_input.lower()
    # raise NotImplementedError ("Get Response Implementation Code missing...")

    if lowered == " ":
        return "Hey, Trainer! Are you still there?"
    elif 'hello' in lowered:
        return "Hello, Trainer!"
    elif 'bye' in lowered:
        return "See you, Trainer!"
    elif 'help' in lowered:
        return "What can I do for you, Trainer?"
    elif 'how are you' in lowered:
        return choice([
            "Doing alright, thanks for asking!",
            "Never better!",
            "Im doing well!"
        ])
    elif 'roll dice' in lowered:
        dice_check: int = randint(1,1024)
        return f' You rolled: {dice_check}'
    else:
        return choice([" Could you repeat that? I dont understand....",
                       "What are you talking about?",
                       "Could you rephrase that?",
                       "I dont know what your talking about?"])