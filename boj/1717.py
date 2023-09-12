import sys


input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
N, M = map(int, input().split())
parent = [i for i in range(N + 1)]


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    x = find(a)
    y = find(b)

    if x > y:
        parent[y] = x
    else:
        parent[x] = y


for _ in range(M):
    num, a, b = map(int, input().split())

    if num == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")