import sys

n = int(input())
dp = [0] * (n + 1)
dp[0], dp[1] = 0, 1

for i in range(2, n + 1):
    _min = sys.maxsize
    j = 1

    while j ** 2 <= i:
        _min = min(_min, dp[i - j ** 2])
        j += 1
    dp[i] = _min + 1

print(dp[n])