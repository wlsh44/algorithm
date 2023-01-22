n = int(input())

dp = [0] * n
dp[0], dp[1] = 1, 1
cnt = 0
for i in range(2, n):
    dp[i] = dp[i - 1] + dp[i - 2]
    cnt += 1
print(dp[n - 1], cnt)