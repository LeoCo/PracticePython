def minus_duplicate(lst):
    set1 = set(lst)
    lst2 = list(set1)
    return lst2

a = [1, 1, 2, 3, 4, 3, 4, 5]

print(minus_duplicate(a))