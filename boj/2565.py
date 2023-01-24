import sys

input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x: x[0])

arr_b = [x[1] for x in arr]
dp = [[x[1]] for x in arr]

for i in range(N):
    for j in range(i):
        if arr_b[j] < arr_b[i]:
            if len(dp[i]) < len(dp[j]) + 1:
                dp[i] = dp[j] + [arr_b[i]]
res = 0
for i in range(N):
    if res < len(dp[i]):
        res = len(dp[i])
print(N - res)
