from collections import deque

n = int(input())
m = int(input())

graph = {i: list() for i in range(1, n + 1)}

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs(start):
    q = deque([(start, 1)])
    visited = set([(start)])
    cnt = 0

    while q:
        x, num = q.popleft()
        if num > 2:
            continue
        for nx in graph[x]:
            if nx in visited:
                continue
            visited.add(nx)
            q.append((nx, num + 1))
            cnt += 1
    return cnt

print(bfs(1))
