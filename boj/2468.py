from collections import deque
import sys

input = sys.stdin.readline
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]


def bfs(y, x, visited, water):
    visited.add((y, x))
    q = deque([(y, x)])

    while q:
        y, x = q.popleft()

        for dy, dx in d:
            ny, nx = y + dy, x + dx

            if (ny, nx) not in visited and 0 <= ny < N and 0 <= nx < N and (ny, nx) not in water:
                visited.add((ny, nx))
                q.append((ny, nx))


max_cnt = 0
for height in range(0, 101):
    cnt = 0

    visited = set([])
    water = set([(i, j) for i in range(N) for j in range(N) if graph[i][j] <= height])
    for i in range(N):
        for j in range(N):
            if (i, j) not in visited and (i, j) not in water:
                bfs(i, j, visited, water)
                cnt += 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)