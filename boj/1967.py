import sys


input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
N = int(input())
tree = {i: [] for i in range(1, N + 1)}


for _ in range(N - 1):
    parent, child, weight = map(int, input().split())
    tree[parent].append((child, weight))
    tree[child].append((parent, weight))


def dfs(node, length):
    for child, weight in tree[node]:
        if distance[child] != -1:
            continue
        distance[child] = length + weight
        dfs(child, length + weight)


distance = [-1] * (N + 1)
distance[1] = 0
dfs(1, 0)

start = distance.index(max(distance))
distance = [-1] * (N + 1)
distance[start] = 0
dfs(start, 0)

print(max(distance))