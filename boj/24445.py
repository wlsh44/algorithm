import sys
from collections import deque

input = sys.stdin.readline
N, M, R = map(int, input().split())

graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for node in graph.values():
    node.sort(reverse=True)
order = 1
res = [0 for _ in range(N + 1)]


def bfs(start):
    global order
    visited = [False for _ in range(N + 1)]
    visited[start] = True
    q = deque([start])

    while q:
        cur_node = q.popleft()
        res[cur_node] = order
        order += 1
        for adj_node in graph[cur_node]:
            if visited[adj_node]:
                continue
            visited[adj_node] = True
            q.append(adj_node)

bfs(R)
for i in range(1, N + 1):
    print(res[i])