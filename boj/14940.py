from collections import deque
import sys


input = sys.stdin.readline
N, M = map(int, input().split())

arr = [[0] * M for _ in range(N)]
res = [[0] * M for _ in range(N)]

y, x = 0, 0
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        if row[j] == 2:
            y, x = i, j
        arr[i][j] = row[j]


def bfs(y, x):
    visited = [[False] * M for _ in range(N)]
    q = deque([(y, x)])

    visited[y][x] = True
    while q:
        y, x = q.popleft()

        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ny, nx = y + dy, x + dx

            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] is False and arr[ny][nx] == 1:
                visited[ny][nx] = True
                res[ny][nx] = res[y][x] + 1
                q.append((ny, nx))


bfs(y, x)
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            print(0, end=" ")
        elif res[i][j] == 0 and not (y == i and x == j):
            print(-1, end=" ")
        else:
            print(res[i][j], end=" ")
    print()
