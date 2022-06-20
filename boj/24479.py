import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int, input().split())

arr = {i: [] for i in range(1, N + 1)}
visited = [0] * (N + 1)
cnt = 1

def dfs(v):
    global cnt
    visited[v] = cnt
    cnt += 1
    for n in arr[v]:
        if visited[n] != 0:
            continue
        dfs(n)


for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

for value in arr.values():
    value.sort()

dfs(R)

for num in range(1, N + 1):
    print(visited[num])
