import sys

input = sys.stdin.readline
d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

res = 0


def dfs(y, x, num, cnt):
    global res
    if cnt == 4:
        res = max(res, num)
        return

    for i in range(4):
        ny, nx = y + d[i][0], x + d[i][1]

        if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(ny, nx, board[ny][nx] + num, cnt + 1)
            visited[ny][nx] = False


def check_T(y, x):
    global res
    for i in range(4):
        num = board[y][x]
        for j in range(3):
            n = (i + j) % 4
            ny, nx = y + d[n][0], x + d[n][1]

            if not (0 <= ny < N and 0 <= nx < M):
                num = 0
                break
            num += board[ny][nx]
        res = max(res, num)


for y in range(N):
    for x in range(M):
        visited[y][x] = True
        dfs(y, x, board[y][x], 1)
        visited[y][x] = False
        check_T(y, x)

print(res)