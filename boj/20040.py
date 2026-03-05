import sys


sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

n, m = map(int, input().split())

p = [i for i in range(n)]

def find(x):
    if p[x] == x:
        return x
    p[x] = find(p[x])
    return p[x]


def union(a, b):
    x = find(a)
    y = find(b)

    if x < y:
        p[x] = y
    else:
        p[y] = x

for ans in range(1, m + 1):
    a, b = map(int, input().split())
    if find(a) == find(b):
        print(ans)
        exit()
    union(a, b)
print(0)