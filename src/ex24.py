def print_board(x):

    line_odd = ""

    for i in range(0,x):
        line_odd += " ---"

    line_even = ""

    for i in range(0,x):
        line_even += "|   "
    line_even += "|"

    for i in range(0, x):
        print(line_odd)
        print(line_even)
    print(line_odd)

print_board(3)