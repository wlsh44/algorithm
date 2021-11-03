from collections import deque
import sys

input = sys.stdin.readline


def dfs(graph, root):
    visited = {}
    s = [root]

    while s:
        v = s.pop()

        if v not in visited:
            visited[v] = True
            s += sorted(graph[v], reverse=True)
    return visited.keys()


def bfs(graph, root):
    visited = {}
    q = deque([root])

    while q:
        v = q.popleft()

        if v not in visited:
            visited[v] = True
            q += sorted(graph[v])
    return visited.keys()


graph = {}
N, M, V = map(int, input().split())
for _ in range(M):
    n1, n2 = map(int, input().split())
    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)
    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)

if V not in graph:
    graph[V] = []
print(' '.join(list(map(str, dfs(graph, V)))))
print(' '.join(list(map(str, bfs(graph, V)))))

