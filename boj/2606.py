import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

arr = [[] for _ in range(n + 1)]
for _ in range(m):
    cur, nxt = map(int, input().split())
    arr[cur].append(nxt)
    arr[nxt].append(cur)

v = [0] * (n + 1)


def dfs(cur):
    cnt = 1
    v[cur] = 1
    for nxt in arr[cur]:
        if v[nxt]:
            continue
        v[nxt] = 1
        cnt += dfs(nxt)
    return cnt

print(dfs(1) - 1)