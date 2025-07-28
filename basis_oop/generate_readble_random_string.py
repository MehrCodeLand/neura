

import generate_sub_random_keyword

def generate(sub_part:int=2, seprator="-"):
    output = ""
    for i in range(sub_part):
        output += generate_sub_random_keyword.generate()
        if i+1 != sub_part:
            output += seprator
    return output


if __name__ == "__main__":
    print(generate())
