import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())

d = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
farms = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
tomatoes = [(z, y, x) for z in range(H) for y in range(N) for x in range(M) if farms[z][y][x] == 1]
dist = [[[0] * M for _ in range(N)] for _ in range(H)]


q = deque([])
def bfs():
    while q:
        z, y, x = q.popleft()

        for dz, dy, dx in d:
            nz, ny, nx = z + dz, y + dy, x + dx

            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and farms[nz][ny][nx] == 0 and \
                    (dist[nz][ny][nx] == 0 or dist[nz][ny][nx] > dist[z][y][x] + 1):
                q.append((nz, ny, nx))
                dist[nz][ny][nx] = dist[z][y][x] + 1


for z, y, x in tomatoes:
    q.append((z, y, x))
bfs()


def get_answer():
    res = 0
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if dist[z][y][x] == 0 and farms[z][y][x] == 0:
                    return -1
                elif res < dist[z][y][x]:
                    res = dist[z][y][x]
    return res


print(get_answer())
