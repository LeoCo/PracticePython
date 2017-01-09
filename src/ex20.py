def is_in_list(x,num):
    length = len(x)
    if length == 1:
        if x[0] == num:
            return True
        else:
            return False

    if length == 2:
        if x[0] == num:
            return True
        elif x[1] == num:
            return True
        else:
            return False

    middle = round(length/2) - 1

    if num < x[middle]:
        return is_in_list(x[0:middle],num)
    else:
        return is_in_list(x[middle:length],num)




a = [1, 3, 5, 30, 42, 43, 500,1000]

print(is_in_list(a,1000))