import random

a = []
b = []

for i in range(0,random.randint(5,10)):
    a.append(random.randint(1,10))

for i in range(0,random.randint(5,10)):
    b.append(random.randint(1,10))

print(a)
print(b)

c = []

c = [x for x in set(a) if (x in b)]

print(c)