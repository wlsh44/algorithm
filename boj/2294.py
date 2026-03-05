n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)
dp = [2e7] * (k + 1)
dp[0] = 0

for i in range(1, k + 1):
    for num in arr:
        if i - num >= 0:
            dp[i] = min(dp[i], dp[i - num] + 1)

print(dp[-1] if dp[-1] != 2e7 else -1)
