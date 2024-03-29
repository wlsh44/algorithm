from collections import deque
import sys

input = sys.stdin.readline
N, L, R = map(int, input().split())

world = [list(map(int, input().split())) for _ in range(N)]


def bfs(y, x, visited, union):
    q = deque([(y, x)])
    visited[y][x] = True

    people = 0
    while q:
        y, x = q.popleft()

        people += world[y][x]
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and L <= abs(world[y][x] - world[ny][nx]) <= R and visited[ny][nx] is False:
                union.append((ny, nx))
                visited[ny][nx] = True
                q.append((ny, nx))
    return people // len(union)


res = 0
flag = True
while flag:
    flag = False
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] is False:
                union = [(i, j)]
                people = bfs(i, j, visited, union)
                if len(union) != 1:
                    flag = True
                for y, x in union:
                    world[y][x] = people
    if flag:
        res += 1
print(res)