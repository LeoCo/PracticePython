
def player_input_move():
    while True:
        move = input("Please insert your move (row, column) from 1 to 3:")
        list1 = move.split(",")
        x = int(list1[0].strip()) - 1
        y = int(list1[1].strip()) - 1
        if (x >= 0 and x <= 2) and (y >= 0 and y <= 2):
            return [x, y]
        print("Input error, please retry")

def draw_board(matrix):

    m = [["","",""],["","",""],["","",""]]

    for i in range(0,3):
        for j in range(0,3):
            if matrix[i][j] == 0:
                m[i][j] = " "
            elif matrix[i][j] == 1:
                m[i][j] = "X"
            else:
                m[i][j] = "O"

    print(" --- --- ---")
    print("| " + m[0][0] + " | " + m[0][1] + " | " + m[0][2] + " |")
    print(" --- --- ---")
    print("| " + m[1][0] + " | " + m[1][1] + " | " + m[1][2] + " |")
    print(" --- --- ---")
    print("| " + m[2][0] + " | " + m[2][1] + " | " + m[2][2] + " |")
    print(" --- --- ---")

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


game = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]

print("Happy game!")

player1 = "Leonardo" #input("Player1 please insert your name: ")
player2 = "Noemi" #input("Player2 please insert your name: ")

draw_board(game)

attempts = 0

while True:
    print(player1 +" is your turn!")
    while True:
        move = player_input_move()
        if game[move[0]][move[1]] == 0:
            game[move[0]][move[1]] = 1
            draw_board(game)
            break
        draw_board(game)
        print("Move not allowed " + player1 + ", please retry")
    attempts += 1
    winner = check_winner(game)
    if winner == 1:
        print("Congratulations " + player1 + " you have won!")
        break
    if winner == 2:
        print("Congratulations " + player2 + " you have won!")
        break

    if attempts == 9:
        print("Congratulations " + player1 + " and " + player2)
        print("This game has no winner, try a new one!")
        break

    print(player2 + " is your turn!")
    while True:
        move = player_input_move()
        if game[move[0]][move[1]] == 0:
            game[move[0]][move[1]] = 2
            draw_board(game)
            break
        draw_board(game)
        print("Move not allowed " + player2 + ", please retry")
    attempts += 1
    winner = check_winner(game)
    if winner == 1:
        print("Congratulations " + player1 + " you have won!")
        break
    if winner == 2:
        print("Congratulations " + player2 + " you have won!")
        break

print("Copyrights by Leo")