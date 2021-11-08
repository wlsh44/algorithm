import sys

input = sys.stdin.readline


def dfs(team, root):
    cycle = []
    s = [root]

    while s:
        v = s.pop()

        if not visited[v]:
            visited[v] = True
            s.append(arr[v])
            cycle.append(v)
        else:
            if v in set(cycle):
                team += cycle[cycle.index(v):]
            return


T = int(input())
for _ in range(T):
    team = []
    n = int(input())
    visited = [False] * (n + 1)
    arr = [0] + list(map(int, input().split()))
    for v in range(1, n + 1):
        if not visited[v]:
            dfs(team, v)
    print(n - len(team))
