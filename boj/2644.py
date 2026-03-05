from collections import deque
import sys


input = sys.stdin.readline
n = int(input())
a, b = map(int, input().split())

m = int(input())
graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs():
    q = deque([(a, 0)])
    visited = {a}

    while q:
        n, dist = q.popleft()

        dist += 1
        for nx in graph[n]:
            if nx == b:
                return dist
            if nx not in visited:
                visited.add(nx)
                q.append((nx, dist))
    return -1


print(dfs())
