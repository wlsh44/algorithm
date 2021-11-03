from collections import deque
import sys


input = sys.stdin.readline
dy = [1, 1, 1, 0, 0, -1, -1, -1]
dx = [1, 0, -1, 1, -1, 1, 0, -1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = [(list(map(int, input().split()))) for _ in range(h)]


    def check(y, x):
        return 0 <= x < w and 0 <= y < h


    def bfs(y, x):
        q = deque([[y, x]])
        graph[y][x] = 0

        while q:
            v = q.popleft()
            for i in range(8):
                ny = v[0] + dy[i]
                nx = v[1] + dx[i]

                if check(ny, nx) and graph[ny][nx] == 1:
                    graph[ny][nx] = 0
                    q += [[ny, nx]]


    cnt = 0
    for y in range(h):
        for x in range(w):
            if graph[y][x] == 1:
                cnt += 1
                bfs(y, x)
    print(cnt)

