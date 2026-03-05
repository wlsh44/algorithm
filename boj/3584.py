import sys

sys.setrecursionlimit(1000000)
T = int(input())


def dfs(tree, d, parent, x, depth):
    d[x] = depth
    for num in tree[x]:
        parent[num] = x
        dfs(tree, d, parent, num, depth + 1)


for _ in range(T):
    N = int(input())

    parent = [0] * (N + 1)
    d = [0] * (N + 1)
    root = set([i for i in range(1, N + 1)])
    tree = {i: [] for i in range(1, N + 1)}
    for _ in range(N - 1):
        A, B = map(int, input().split())
        tree[A].append(B)
        root.remove(B)
    root = list(root)[0]
    A, B = map(int, input().split())
    dfs(tree, d, parent, root, 0)

    while d[A] != d[B]:
        if d[A] > d[B]:
            A = parent[A]
        else:
            B = parent[B]

    while A != B:
        A = parent[A]
        B = parent[B]

    print(A)
