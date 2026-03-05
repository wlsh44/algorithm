from collections import deque
import sys


input = sys.stdin.readline
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(y, x, visited, remove):
    visited[y][x] = True
    q = deque([(y, x)])

    while q:
        y, x = q.popleft()

        for dy, dx in d:
            ny, nx = y + dy, x + dx

            if 0 <= ny < N and 0 <= nx < M:
                if arr[ny][nx] != 0 and visited[ny][nx] is False:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                if arr[ny][nx] == 0:
                    remove[y][x] += 1


ans = 0
while True:
    visited = [[False] * M for _ in range(N)]
    remove = [[0] * M for _ in range(N)]
    cnt = 0
    for y in range(N):
        for x in range(M):
            if visited[y][x] is False and arr[y][x] != 0:
                bfs(y, x, visited, remove)
                cnt += 1
    if cnt == 0:
        print(0)
        break
    elif cnt == 1:
        for y in range(N):
            for x in range(M):
                if arr[y][x] != 0:
                    arr[y][x] = max(arr[y][x] - remove[y][x], 0)
        ans += 1
    else:
        print(ans)
        break
