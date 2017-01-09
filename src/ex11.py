

def divisors(number):
    divisors = [0, 1]

    for i in range(2, number):
        if (number % i) == 0:
            divisors.append(i)

    return divisors

num = int(input("Give me a number: "))

div = divisors(num)

if div == [0,1]:
    print("The number " + str(num) + " is a prime number")
else:
    print("The number " + str(num) + " is not a prime number")

primes = [0, 1]

for i in range(2,num):
    div = divisors(i)
    if div == [0, 1]:
        primes.append(i)

print("This is the list of prime numbers until " + str(num))
print(primes)
print("There are " + str(len(primes)) + " numbers")