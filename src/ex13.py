
def fibonacci(num = 4):
    fib = [1, 1, 2]

    for i in range(3,num):
        fib_current = fib[i-1] + fib[i-2]
        fib.append(fib_current)

    return fib

num = int(input("Enter a number: "))

print(fibonacci(num))