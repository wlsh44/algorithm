from collections import deque

N, M = map(int, input().split())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
graph = [list(map(int, input())) for _ in range(N)]

res = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            continue

        dq = deque([(i, j)])
        while len(dq) != 0:
            y, x = dq.popleft()

            for k in range(4):
                ny, nx = y + dy[k], x + dx[k]
                if ny >= 0 and ny < N and nx >= 0 and nx < M and graph[ny][nx] == 0:
                    graph[ny][nx] = 1
                    dq.append((ny, nx))
        res += 1
print(res)
