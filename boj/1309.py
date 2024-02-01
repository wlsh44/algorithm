n = int(input())

dp = [1, 1, 1]

for i in range(1, n):
    tmp1, tmp2, tmp3 = dp[0], dp[1], dp[2]
    dp[0] = tmp1 + tmp2 + tmp3
    dp[1] = tmp1 + tmp3
    dp[2] = tmp1 + tmp2
print(sum(dp) % 9901)