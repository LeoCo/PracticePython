import time

a = "My name is Michele"


def time_execution(code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time

def reverse(str):
    divided = str.split()
    loops = len(divided) - 1
    res = []
    for i in range(loops,-1,-1):
        res.append(divided[i])
    return " ".join(res)

def reverseWord(w):
  return ' '.join(w.split()[::-1])

print(reverse(a))

print(time_execution('reverse("My name is MicheleMy name is MicheleMy name is Michele")'))
print(time_execution('reverseWord("My name is MicheleMy name is MicheleMy name is Michele")'))