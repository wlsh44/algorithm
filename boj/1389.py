from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

connection = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    u, v = map(int, input().split())
    connection[u].append(v)
    connection[v].append(u)


def bfs(start):
    dist = [0] * (N + 1)
    q = deque([start])

    res = 0
    while q:
        u = q.popleft()

        for v in connection[u]:
            if v != start and dist[v] == 0:
                q.append(v)
                dist[v] += dist[u] + 1
                res += dist[v]
    return res


ans = 0
min_bacon = sys.maxsize
for i in range(1, N + 1):
    cnt = bfs(i)
    if cnt < min_bacon:
        min_bacon = cnt
        ans = i
print(ans)
