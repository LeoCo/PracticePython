import random

lower_bound = 0
upper_bound = 10

guess = 0

attempt = 0

while True:

    guess = random.randint(lower_bound, upper_bound)

    guess_bool = input("Is " + str(guess) + " your number? y/n: ")
    attempt += 1

    if guess_bool == "y":
        break

    lower = input("Is your number lower? y/n: ")

    if lower == "y":
        upper_bound = guess - 1
    else:
        lower_bound = guess + 1


print("Your number is " + str(guess))
print("It took me " + str(attempt) + " attempts")