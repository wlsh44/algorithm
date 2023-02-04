import sys
from collections import deque

MAX = 100000

N, K = map(int, input().split())


def bfs(x):
    q = deque([(x, 0)])
    visited = {x}

    res = sys.maxsize
    while q:
        node, time = q.popleft()

        if node == K and time < res:
            res = time
        if 0 <= node - 1 <= MAX and node - 1 not in visited:
            q.append((node - 1, time + 1))
            visited.add(node - 1)
        if 0 <= node * 2 <= MAX and node * 2 not in visited:
            q.append((node * 2, time))
            visited.add(node * 2)
        if 0 <= node + 1 <= MAX and node + 1 not in visited:
            q.append((node + 1, time + 1))
            visited.add(node + 1)
    return res
print(bfs(N))