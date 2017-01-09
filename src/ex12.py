
a = [5, 10, 15, 20, 25]

def first_last(lst):
    last = len(lst) - 1
    return [lst[0], lst[last]]

print(first_last(a))