N, M = map(int, input().split())
y, x, vec = map(int, input().split())

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
res = 0
while True:
    i = 0
    while i < 4:
        if vec - 1 == -1:
            vec = 3
        else:
            vec -= 1
        nx, ny = x + dx[vec], y + dy[vec]
        if not(nx < 0 or nx >= M or ny < 0 or ny >= N or visit[ny][nx] is True or arr[ny][nx] == 1):
            x, y = nx, ny
            visit[y][x] = True
            res += 1
            break
        i += 1
    if i == 4 and arr[y + dy[(vec + 2) % 4]][x + dx[(vec + 2) % 4]] == 1:
        break
    elif i == 4:
        x += dx[(vec + 2) % 4]
        y += dy[(vec + 2) % 4]
print(res)
