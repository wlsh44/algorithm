import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [0] + list(map(int, input().split()))

dp = [0] * (N + 1)
dp[0] = arr[0]
for i in range(1, N + 1):
    dp[i] = dp[i - 1] + arr[i]

for _ in range(M):
    i, j = map(int, input().split())

    print(dp[j] - dp[i - 1])
