import random


def cows_bulls(num1,num2):
    cows = 0
    bulls = 0

    #cows
    for i in range(0,4):
        if num1[i] == num2[i]:
            cows += 1

    #bulls
    for i in range(0,4):
        bulls += num1.count(num2[i])
        if num1[i] == num2[i]:
            bulls -= 1

    return cows, bulls

def random_4int():
    voc = "0123456789"
    return ''.join((random.sample(voc,4)))


if __name__ == "__main__":
    print("Happy game!")

    num1 = random_4int()

    #Solution
    #print(num1)

    attempts = 0

    while True:
        num2 = input("Enter a number: ")
        attempts +=1
        cows, bulls = cows_bulls(num1,num2)
        print(str(cows) + " Cows, " + str(bulls) + " Bulls")
        if cows == 4:
            print("You won!")
            print("With " + str(attempts) + " attempts")
            break


