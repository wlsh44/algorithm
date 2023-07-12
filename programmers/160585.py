from itertools import permutations


def is_finished(board, team):
    for i in range(3):
        if board[i][0] == team and board[i][1] == team and board[i][2] == team:
            return True
    for i in range(3):
        if board[0][i] == team and board[1][i] == team and board[2][i] == team:
            return True
    if board[0][0] == team and board[1][1] == team and board[2][2] == team:
        return True
    if board[2][0] == team and board[1][1] == team and board[0][2] == team:
        return True
    return False


def play(board, o, x):
    if len(o) < len(x):
        return False
    i, j = 0, 0
    while True:
        if i == len(o):
            break
        board[o[i][0]][o[i][1]] = 1
        i += 1
        if is_finished(board, 1):
            break

        if j == len(x):
            break
        board[x[j][0]][x[j][1]] = 2
        j += 1
        if is_finished(board, 2):
            break

    return i == len(o) and j == len(x)


def solution(board):
    answer = 1

    o, x = [], []
    for i in range(3):
        for j in range(3):
            if board[i][j] == "O":
                o.append((i, j))
            if board[i][j] == "X":
                x.append((i, j))

    for op in permutations(o, len(o)):
        for xp in permutations(x, len(x)):
            new_board = [[0] * 3 for _ in range(3)]
            if play(new_board, op, xp):
                return 1
    return 0