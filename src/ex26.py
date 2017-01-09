

def check_winner(matrix):

    length = len(matrix)

    # check rows
    for i in range(0,length):
        count1 = 0
        count2 = 0
        for j in range(0, length):
            if matrix[i][j] == 2:
                count2 += 1
            if matrix[i][j] == 1:
                count1 += 1
        if count2 == length:
            return 2
        if count1 == length:
            return 1

    # check colums
    for i in range(0,length):
        count1 = 0
        count2 = 0
        for j in range(0, length):
            if matrix[j][i] == 2:
                count2 += 1
            if matrix[j][i] == 1:
                count1 += 1
        if count2 == length:
            return 2
        if count1 == length:
            return 1

    # check diagonals1
    count1 = 0
    count2 = 0
    for i in range(0,length):
        if matrix[i][i] == 2:
            count2 += 1
        if matrix[i][i] == 1:
            count1 += 1
    if count2 == length:
        return 2
    if count1 == length:
        return 1

    # check diagonals2
    count1 = 0
    count2 = 0
    for i in range(0, length):
        if matrix[i][length - 1 - i] == 2:
            count2 += 1
        if matrix[i][length - 1 - i] == 1:
            count1 += 1
    if count2 == length:
        return 2
    if count1 == length:
        return 1

    return 0


winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]

print(str(check_winner(winner_is_2)))
print(str(check_winner(winner_is_1)))
print(str(check_winner(winner_is_also_1)))
print(str(check_winner(no_winner)))
print(str(check_winner(also_no_winner)))