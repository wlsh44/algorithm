from collections import deque
import sys


def bfs(root):
    q = deque([root])

    while q:
        v = q.popleft()

        if v not in visited:
            visited[v] = True
            q += graph[v]


input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = {}

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
for n in range(1, N + 1):
    if n not in visited:
        bfs(n)
        cnt += 1
print(cnt)
