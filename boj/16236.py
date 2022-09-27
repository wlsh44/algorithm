from collections import deque

N = int(input())
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]


x, y = 0, 0
arr = [list(map(int, input().split())) for _ in range(N)]
size = 2
res = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            x, y = j, i
            break


def bfs(x, y, size):
    t = 0
    q = deque([(y, x)])
    v = [[False] * N for _ in range(N)]
    dist = [[0] * N for _ in range(N)]
    v[y][x] = True
    tmp = []
    while q:
        y, x = q.popleft()
        t += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= ny < N and 0 <= nx < N and v[ny][nx] == False and arr[ny][nx] <= size:
                q.append((ny, nx))
                v[ny][nx] = True
                dist[ny][nx] = dist[y][x] + 1
                if arr[ny][nx] < size and arr[ny][nx] != 0:
                    tmp.append((ny, nx, dist[ny][nx]))
    return deque(sorted(tmp, key=lambda x: (x[2], x[0], x[1])))

cnt = 0
res = 0
while True:
    next_fish = bfs(x, y, size)
    if len(next_fish) == 0:
        break

    fish_y, fish_x, time = next_fish.popleft()
    res += time
    arr[y][x] = 0
    arr[fish_y][fish_x] = 0
    x, y = fish_x, fish_y
    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0
print(res)
