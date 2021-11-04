import sys

input = sys.stdin.readline


def dfs(root):
    s = [root]

    while s:
        v = s.pop()

        if v not in visited:
            visited[v] = True
            s += graph[v]


T = int(input())
for _ in range(T):
    N = int(input())
    graph = [[] for _ in range(N + 1)]
    visited = {}
    cnt = 0
    arr = list(map(int, input().split()))
    for i, n in enumerate(arr):
        graph[i + 1].append(n)
    for n in range(1, N + 1):
        if n not in visited:
            dfs(n)
            cnt += 1
    print(cnt)