import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
graph = {i: [] for i in range(1, N + 1)}

for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
res = [0 for _ in range(N + 1)]


def bfs(start):
    visited = [False for _ in range(N + 1)]
    visited[start] = True
    q = deque([start])

    while q:
        cur_node = q.popleft()

        for adj_node in graph[cur_node]:
            if visited[adj_node]:
                continue
            visited[adj_node] = True
            q.append(adj_node)
            res[adj_node] = cur_node


bfs(1)
for i in range(2, N + 1):
    print(res[i])