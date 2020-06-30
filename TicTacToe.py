import random

board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def printBoard(board):
    print(board[0][0] + '|' + board[0][1] + '|' + board[0][2])
    print('-+-+-')
    print(board[1][0] + '|' + board[1][1] + '|' + board[1][2])
    print('-+-+-')
    print(board[2][0] + '|' + board[2][1] + '|' + board[2][2])


dict = {7: [0, 0], 8: [0, 1], 9: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 1: [2, 0], 2: [2, 1], 3: [2, 2]}
dict
pos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count = 0


def check(x):
    win = 0
    if board[a][0] == board[a][1] == board[a][2] == x:
        win = 1
        return win
    if board[0][b] == board[1][b] == board[2][b] == x:
        win = 1
        return win
    if a == b:
        if board[0][0] == board[1][1] == board[2][2]:
            win = 1
            return win

    if a + b == 2:
        if board[2][0] == board[1][1] == board[0][2]:
            win = 1
            return win

    return win


while True:
    printBoard(board)
    win = 0
    x = int(input('Enter'))
    a, b = dict[x][0], dict[x][1]
    if board[a][b] == ' ':
        board[a][b] = 'X'
        count += 1
        pos.remove(x)

        if check(board[a][b]) == 1:
            printBoard(board)
            print('You Win!')
            break

    if count <= 8:
        y = random.choice(pos)
        a, b = dict[y][0], dict[y][1]
        board[a][b] = 'O'
        count += 1
        pos.remove(y)

        if check(board[a][b]) == 1:
            printBoard(board)
            print('Computer Wins!')
            break

    if count == 9:
        printBoard(board)
        print('Its a Tie')
        break
