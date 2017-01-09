import re

d = {}

with open('Training_01.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        text = re.search(r'/.*/(.*)/.*',str(line)).group(1)
        #print(text)
        #text = line = line[3:-26]
        if (text in d):
            d[text] += 1
        else:
            d[text] = 1
        line = open_file.readline()
print(d)