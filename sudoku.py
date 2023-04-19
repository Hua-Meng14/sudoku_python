from random import randint, shuffle


def printBoard(board):

    boardString = ""
    for i in range(9):
        for j in range(9):
            boardString += str(board[i][j]) + " "
            if (j+1) % 3 == 0 and j != 0 and j + 1 != 9:
                boardString += "| "

            if j == 8:
                boardString += "\n"

            if j == 8 and (i+1) % 3 == 0 and i + 1 != 9:
                boardString += "---------------------\n"

    print(boardString)


def findEmpty(board):

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)

    return None


def valid(board, position, number):

    for i in range(9):
        if board[i][position[1]] == number:
            return False

    for j in range(9):
        if board[position[0]][j] == number:
            return False

    startI = position[0] - position[0] % 3
    startJ = position[1] - position[1] % 3

    for i in range(3):
        for j in range(3):
            if board[startI + i][startJ + j] == number:
                return False
    return True


def solve(board):
    empty = findEmpty(board)
    if not empty:
        return True
    for numbers in range(1, 10):
        if valid(board, empty, numbers):
            board[empty[0]][empty[1]] = numbers

            if solve(board):
                return True
            board[empty[0]][empty[1]] = 0
    return False


def generateBoard():
    board = [[0 for i in range(9)] for j in range(9)]

    for i in range(0, 9, 3):
        numbers = list(range(1, 10))
        shuffle(numbers)
        for row in range(3):
            for column in range(3):
                board[i + row][i + column] = numbers.pop()

    def fillCell(board, row, column):
        if row == 9:
            return True

        if column == 9:
            return fillCell(board, row + 1, 0)

        if board[row][column] != 0:
            return fillCell(board, row, column + 1)

        for number in range(1, 10):
            if valid(board, (row, column), number):
                board[row][column] = number

                if fillCell(board, row, column + 1):
                    return True
        board[row][column] = 0
        return False

    fillCell(board, 0, 0)

    for _ in range(randint(55, 65)):
        row, col = randint(0, 8), randint(0, 8)
        board[row][col] = 0

    return board

if __name__ == "__main__":
    board = generateBoard()
    print("Problem Board:")
    printBoard(board)
    solve(board)
    print("Solved Board:")
    printBoard(board)
