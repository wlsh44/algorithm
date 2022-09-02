import sys
from collections import deque


input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().rstrip())) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    q = deque([(x, y)])
    arr[y][x] = 0
    cnt = 1

    while q:
        v = q.popleft()

        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < N and arr[ny][nx] == 1:
                cnt += 1
                arr[ny][nx] = 0
                q.append((nx, ny))
    return cnt


total = 0
res = []
for y in range(N):
    for x in range(N):
        if arr[y][x] == 1:
            total += 1
            res.append(bfs(x, y))
res.sort()

print(total)
for num in res:
    print(num)