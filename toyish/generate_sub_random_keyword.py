import random 

def generate()->str:
    char_set_1:str = "qwrtypsdfghjklzxcvbnm"
    char_set_2:str = "eiaou"
    return random.choice(char_set_1) + random.choice(char_set_2) + random.choice(char_set_1) + random.choice(char_set_2)


if __name__ == "__main__":
    print(generate())



