H, W = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(H)]
for i in range(H):
    tmp = list(map(int, input().split()))
    for j in range(W):
        arr[i][j] = (arr[i][j] - tmp[j]) ** 2

dp = [[0] * W for _ in range(H)]

dp[0] = arr[0]

for i in range(1, H):
    for j in range(W):
        if W == 1:
            dp[i][j] = arr[i][j] + dp[i - 1][j]
        elif j == 0:
            dp[i][j] = arr[i][j] + min(dp[i - 1][j], dp[i - 1][j + 1])
        elif j == W - 1:
            dp[i][j] = arr[i][j] + min(dp[i - 1][j], dp[i - 1][j - 1])
        else:
            dp[i][j] = arr[i][j] + min(dp[i - 1][j], dp[i - 1][j + 1], dp[i - 1][j - 1])
print(min(dp[len(dp) - 1]))
