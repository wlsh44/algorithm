import sys

input = sys.stdin.readline

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

res = 0
for i in range(N):
    for j in range(N):
        res = max(res, board[i][j])

def move_left(cur_board):
    global res
    for i in range(N):
        for j in range(N):
            nx = j
            while 0 < nx < N and cur_board[i][nx - 1] == 0:
                cur_board[i][nx - 1] = cur_board[i][nx]
                cur_board[i][nx] = 0
                nx -= 1
            if nx == 0:
                continue
            if cur_board[i][nx] == cur_board[i][nx - 1] and new_block[i][nx - 1] is False:
                cur_board[i][nx - 1] *= 2
                res = max(res, cur_board[i][nx - 1])
                cur_board[i][nx] = 0
                new_block[i][nx - 1] = True

def move_right(cur_board):
    global res
    for i in range(N):
        for j in range(N - 1, -1, -1):
            nx = j
            while 0 <= nx < N - 1 and cur_board[i][nx + 1] == 0:
                cur_board[i][nx + 1] = cur_board[i][nx]
                cur_board[i][nx] = 0
                nx += 1
            if nx == N - 1:
                continue
            if cur_board[i][nx] == cur_board[i][nx + 1] and new_block[i][nx + 1] is False:
                cur_board[i][nx + 1] *= 2
                res = max(res, cur_board[i][nx + 1])
                cur_board[i][nx] = 0
                new_block[i][nx + 1] = True

def move_up(cur_board):
    global res
    for j in range(N):
        for i in range(N):
            ny = i
            while 0 < ny < N and cur_board[ny - 1][j] == 0:
                cur_board[ny - 1][j] = cur_board[ny][j]
                cur_board[ny][j] = 0
                ny -= 1
            if ny == 0:
                continue
            if cur_board[ny][j] == cur_board[ny - 1][j] and new_block[ny - 1][j] is False:
                cur_board[ny - 1][j] *= 2
                res = max(res, cur_board[ny - 1][j])
                cur_board[ny][j] = 0
                new_block[ny - 1][j] = True

def move_down(cur_board):
    global res
    for j in range(N):
        for i in range(N - 1, -1, -1):
            ny = i
            while 0 <= ny < N - 1 and cur_board[ny + 1][j] == 0:
                cur_board[ny + 1][j] = cur_board[ny][j]
                cur_board[ny][j] = 0
                ny += 1
            if ny == N - 1:
                continue
            if cur_board[ny][j] == cur_board[ny + 1][j] and new_block[ny + 1][j] is False:
                cur_board[ny + 1][j] *= 2
                res = max(res, cur_board[ny + 1][j])
                cur_board[ny][j] = 0
                new_block[ny + 1][j] = True

q = [board]
for _ in range(5):
    next_q = []
    while q:
        new_block = [[False] * N for _ in range(N)]
        cur_board = q.pop()

        new_board = [row[:] for row in cur_board]
        move_down(new_board)
        next_q.append(new_board)

        new_board = [row[:] for row in cur_board]
        move_up(new_board)
        next_q.append(new_board)

        new_board = [row[:] for row in cur_board]
        move_left(new_board)
        next_q.append(new_board)

        new_board = [row[:] for row in cur_board]
        move_right(new_board)
        next_q.append(new_board)

    q = next_q
print(res)
