word = "yamamay"

reverse_iter = len(word) - 1

pal = True

for i in word:
    condition = i == word[reverse_iter]
    if not condition:
        pal = False
        break
    reverse_iter -= 1

print(pal)