import sys
from collections import deque


input = sys.stdin.readline

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
N, M, K = map(int, input().split())

graph = [[0] * M for _ in range(N)]
visited = set()
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            graph[y][x] = 1


def bfs(x, y):
    visited.add((x, y))
    q = deque([(x, y)])

    size = 0
    while q:
        x, y = q.popleft()

        size += 1
        for dy, dx in d:
            ny, nx = y + dy, x + dx

            if 0 <= ny < N and 0 <= nx < M and (nx, ny) not in visited and graph[ny][nx] == 0:
                visited.add((nx, ny))
                q.append((nx, ny))
    return size


ans = []
for y in range(N):
    for x in range(M):
        if (x, y) not in visited and graph[y][x] == 0:
            ans.append(bfs(x, y))

ans.sort()
print(len(ans))
print(*ans)

