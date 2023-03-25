import sys

input = sys.stdin.readline
sys.setrecursionlimit(int(1e7))

N, M, R = map(int, input().split())

visited = [False for _ in range(N + 1)]
graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for node in graph.values():
    node.sort(reverse=True)

res = [0 for i in range(N + 1)]

seq = 1
def dfs(R):
    global seq

    visited[R] = True
    res[R] = seq
    seq += 1
    for node in graph[R]:
        if visited[node]:
            continue
        dfs(node)


dfs(R)
for i in range(1, N + 1):
    print(res[i])