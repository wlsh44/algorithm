from collections import deque
import sys


input = sys.stdin.readline
N, M = map(int, input().split())

graph = [list(input()) for _ in range(N)]

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
dist = [[[0] * 2 for _ in range(M)] for _ in range(N)]
dist[0][0][0] = 1


def bfs():
    q = deque([(0, 0, 0)])

    while q:
        broke, y, x = q.popleft()

        if y == N - 1 and x == M - 1:
            return dist[y][x][broke]
        for d in move:
            ny, nx = y + d[0], x + d[1]

            if 0 <= ny < N and 0 <= nx < M:
                if graph[ny][nx] == "1" and broke == 0:
                    dist[ny][nx][1] = dist[y][x][0] + 1
                    q.append((1, ny, nx))
                elif graph[ny][nx] == "0" and dist[ny][nx][broke] == 0:
                    dist[ny][nx][broke] = dist[y][x][broke] + 1
                    q.append((broke, ny, nx))
    return -1


print(bfs())