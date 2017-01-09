import random

def pass_gen(length = 10, strong = True):
    letters = "abcdefghilmnopqrstuvz"
    numbers =  "01234567890"
    specials = "_-.!$%"

    dictionary = letters
    if strong == True:
        dictionary += numbers + specials

    dictionary = list(dictionary)

    dic_length = len(dictionary) - 1

    password = []

    for i in range(0,length):
        num = random.randint(0,dic_length)
        letter = dictionary[num]
        password.append(letter)

    return "".join(password)

print(pass_gen(length = 20, strong = True))