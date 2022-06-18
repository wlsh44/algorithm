from collections import deque

N, M = map(int, input().split())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
graph = [list(map(int, input())) for _ in range(N)]

res = 1
x, y = 0, 0
dq = deque([(y, x)])
while len(dq) != 0:
    y, x = dq.popleft()
    flag = False
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 1:
            graph[ny][nx] = graph[y][x] + 1
            dq.append((ny, nx))
print(graph[N - 1][M - 1])
