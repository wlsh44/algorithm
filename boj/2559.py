import sys

input = sys.stdin.readline
N, K = map(int, input().split())
arr = [*map(int, input().split())]
num = 0
for i in range(K):
    num += arr[i]

res = num
for i in range(1, N - K + 1):
    num = num - arr[i - 1] + arr[i + K - 1]
    if res < num:
        res = num
print(res)

