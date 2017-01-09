
#Read Prime

prime = []

with open('primenumbers.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        prime.append(int(line))
        line = open_file.readline()

#Read Happy

happy = []

with open('happynumbers.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        happy.append(int(line))
        line = open_file.readline()

#compare

subset = []

for x in prime:
    if x in happy:
        subset.append(x)

print(subset)