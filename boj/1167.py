import sys


input = sys.stdin.readline
N = int(input())
tree = {i: [] for i in range(1, N + 1)}
for _ in range(N):
    arr = list(map(int, input().split()))
    a = arr[0]
    for i in range(1, len(arr) - 1, 2):
        b, weight = arr[i], arr[i + 1]
        tree[a].append((b, weight))

def dfs(node, length):
    for n, w in tree[node]:
        if distance[n] != -1:
            continue
        distance[n] = length + w
        dfs(n, length + w)


distance = [-1] * (N + 1)
distance[1] = 0
dfs(1, 0)

start = distance.index(max(distance))
distance = [-1] * (N + 1)
distance[start] = 0
dfs(start, 0)
print(max(distance))