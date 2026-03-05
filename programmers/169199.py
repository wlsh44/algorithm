from collections import deque


def bfs(board, r, g):
    q = deque([(r, 0)])
    visited = [[False] * len(board[0]) for _ in range(len(board))]
    visited[r[0]][r[1]] = True
    start = r

    while q:
        r, cnt = q.popleft()

        if r == g:
            return cnt
        if r == start and cnt != 0:
            continue
        for i, d in enumerate([(1, 0), (-1, 0), (0, 1), (0, -1)]):
            dy, dx = d
            ny, nx = r
            while 0 <= ny + dy < len(board) and 0 <= nx + dx < len(board[0]) and board[ny + dy][nx + dx] != "D":
                ny += dy
                nx += dx
            if visited[ny][nx] is True:
                continue
            q.append(((ny, nx), cnt + 1))
            visited[ny][nx] = True
    return -1


def solution(board):
    answer = 0
    r, g = (), ()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "R":
                r = (i, j)
            elif board[i][j] == "G":
                g = (i, j)
    board = [list(row) for row in board]

    return bfs(board, r, g)