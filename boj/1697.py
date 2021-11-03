from collections import deque


MAX = 100001


def bfs(root, k, dist):
    visited = {}
    q = deque([root])

    while q:
        v = q.popleft()

        if v == k:
            break
        if v not in visited:
            visited[v] = True
            for nx in [v - 1, v + 1, v * 2]:
                if 0 <= nx < MAX and not dist[nx]:
                    dist[nx] += dist[v] + 1
                    q += [nx]

    return dist[v]


N, K = map(int, input().split())
dist = [0] * (MAX + 1)
print(bfs(N, K, dist))