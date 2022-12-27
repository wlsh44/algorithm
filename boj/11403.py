from collections import deque
import sys

input = sys.stdin.readline
N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]


def bfs(start, visited):
    q = deque([start])
    visited[start] = True

    while q:
        cur = q.popleft()

        for i in range(N):
            if arr[cur][i] == 1 and (cur == start or (cur != start and arr[start][i] == 0)):
                if not visited[i]:
                    q.append(i)
                    visited[i] = True
                arr[start][i] = 1


for i in range(N):
    visited = [False] * N
    bfs(i, visited)

for row in arr:
    print(*row)