from collections import deque

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def bfs():
    q = deque([0, 0])
    visited = {}
    tmp = {}

    while q:
        y, x = q.popleft()

        for dy, dx in d:
            ny, nx = y + dy, x + dx

            if 0 <= ny < N and 0 <= nx < M:
                if (ny, nx) not in visited:
                    

