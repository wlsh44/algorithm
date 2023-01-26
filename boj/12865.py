import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: x[1])

dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    w, v = arr[i - 1][0], arr[i - 1][1]
    for j in range(1, K + 1):
        if w > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], v + dp[i - 1][j - w])
print(dp[N][K])