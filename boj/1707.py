from collections import deque
import sys


input = sys.stdin.readline


def bfs(root):
    q = deque([root])
    set_ = 1
    visited[root][1] = set_
    while q:
        v = q.popleft()
        if not visited[v][0]:
            visited[v][0] = True
            q += graph[v]
            if visited[v][1] == 1:
                set_ = -1
            else:
                set_ = 1
            for nxt in graph[v]:
                if visited[nxt][1] == visited[v][1]:
                    return False
                if visited[nxt][1] == 0:
                    visited[nxt][1] = set_
    return True


K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [[False, 0] for _ in range(V + 1)]
    flag = True
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    for n in range(1, V + 1):
        if visited[n][1] == 0:
            if not bfs(n):
                flag = False
                break
    print("YES") if flag else print("NO")
