import sys
from collections import deque


input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N, K = map(int, input().split())

    cost = list(map(int, input().split()))

    g = {i: [] for i in range(1, N + 1)}
    indegrees = {i: 0 for i in range(N + 1)}
    for _ in range(K):
        a, b = map(int, input().split())
        g[a].append(b)
        indegrees[b] += 1
    W = int(input())
    dp = [-1] * (N + 1)
    q = deque([])
    for i in range(1, N + 1):
        if indegrees[i] == 0:
            q.append(i)
            dp[i] = cost[i - 1]
    while q:
        x = q.popleft()
        for nx in g[x]:
            indegrees[nx] -= 1
            if indegrees[nx] == 0:
                q.append(nx)
            dp[nx] = max(dp[nx], dp[x] + cost[nx - 1])
    print(dp[W] if dp[W] != -1 else cost[W - 1])
