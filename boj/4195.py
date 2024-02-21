import sys


input = sys.stdin.readline
T = int(input())


def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    x = find(a)
    y = find(b)

    if x != y:
        parent[y] = x
        num[x] += num[y]


for _ in range(T):
    F = int(input())
    parent, num = {}, {}
    for _ in range(F):
        a, b = input().strip().split()
        if a not in parent:
            parent[a] = a
            num[a] = 1
        if b not in parent:
            parent[b] = b
            num[b] = 1
        union(a, b)

        print(num[find(a)])
