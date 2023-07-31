import sys

N = int(input())

arr = [i // 5 if i % 5 == 0 else sys.maxsize for i in range(100001)]
arr[0] = 0
arr[1] = 0
arr[2] = 1
arr[3] = 0
for i in range(4, N + 1):
    if i % 5 == 0:
        continue
    arr[i] = min(arr[i - 2], arr[i]) + 1
print(arr[N] if arr[N] != 0 else -1)