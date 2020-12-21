from random import randrange


def DisplayBoard(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[0][0], "  |  ", board[0][1], "  |  ", board[0][2], "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[1][0], "  |  ", board[1][1], "  |  ", board[1][2], "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[2][0], "  |  ", board[2][1], "  |  ", board[2][2], "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")


def EnterMove(board):
    while True:
        move = int(input("Enter your move:"))

        if move in [i for i in range(1, 10)]:
            move -= 1
            if isinstance(board[move // 3][move % 3], int):
                board[move // 3][move % 3] = 'O'
                DisplayBoard(board)
                break
        print("The move you've entered is not valid or the field is occupied")


def MakeListOfFreeFields(board):
    #
    # the function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers
    #
    emptys = []
    for i in range(3):
        for j in range(3):
            if isinstance(board[i][j], int):
                emptys.append((i, j))

    return emptys


def VictoryFor(board, sign):
    #
    # the function analyzes the board status in order to check if
    # the player using 'O's or 'X's has won the game
    #
    for x in board:
        if x == [sign, sign, sign]:
            return True

    for i in range(3):
        temp = [row[i] for row in board]
        if temp == [sign, sign, sign]:
            return True

    if [board[i][i] for i in range(3)] == [sign, sign, sign]:
        return True

    if [board[i][-i - 1] for i in range(0, 3)] == [sign, sign, sign]:
        return True

    return False


def DrawMove(board):
    #
    # the function draws the computer's move and updates the board
    #
    emptys = MakeListOfFreeFields(board)
    x, y = emptys[randrange(len(emptys))]
    if not x is None:
        board[x][y] = 'X'
        DisplayBoard(board)


######################################################################

board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]

DisplayBoard(board)

while MakeListOfFreeFields(board):
    EnterMove(board)
    if MakeListOfFreeFields(board):
        DrawMove(board)
        if VictoryFor(board, 'O'):
            print("You won!")
            break
        if VictoryFor(board, 'X'):
            print("You lost!")
            break

