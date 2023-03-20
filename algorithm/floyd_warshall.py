import sys

input = sys.stdin.readline

INF = int(1e9)
N = int(input())
M = int(input())
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(M):
    v, u, w = map(int, input().split())
    graph[v][u] = min(graph[v][u], w)


def floyd_warshall():
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


floyd_warshall()
for i in range(1, N + 1):
    for j in range(1, N + 1):
        print(graph[i][j] if graph[i][j] != INF else 0, end=" ")
    print()