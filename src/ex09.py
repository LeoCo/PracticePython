import random

num = random.randint(1,9)

games = 0

victory = False

while True:

    guess = int(input("Try to guess 1-9: "))

    games += 1

    if guess == num:
        victory = True
        break
    elif guess < num:
        print("Guess to low")
    else:
        print("Guess to high")

#    if input("exit or retry?: ") == 'exit':
#        break

if victory:
    print("Congrats you won")
else:
    print("Sorry you lost")
print("With " + str(games) + " games played!")