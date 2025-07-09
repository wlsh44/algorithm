import sys

sys.setrecursionlimit(10 ** 9)


input = sys.stdin.readline
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
dp = [[-1] * M for _ in range(N)]


def dfs(y, x):
    if y == N - 1 and x == M - 1:
        return 1

    if dp[y][x] != -1:
        return dp[y][x]
    dp[y][x] = 0
    for i in range(4):
        ny, nx = d[i][0] + y, d[i][1] + x
        if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] < arr[y][x]:
            dp[y][x] += dfs(ny, nx)
    return dp[y][x]


print(dfs(0, 0))
