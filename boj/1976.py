import sys


input = sys.stdin.readline

N = int(input())
M = int(input())

p = [i for i in range(N + 1)]


def find(x):
    if p[x] == x:
        return x
    p[x] = find(p[x])
    return p[x]


def union(a, b):
    x, y = find(a), find(b)

    if x > y:
        p[y] = x
    else:
        p[x] = y


for i in range(1, N + 1):
    row = list(map(int, input().split()))
    for j in range(1, N + 1):
        if row[j - 1] == 1:
            union(i, j)

travel = list(map(int, input().split()))
city = find(travel[0])
for i in range(1, len(travel)):
    if city != find(travel[i]):
        print("NO")
        exit()
print("YES")

