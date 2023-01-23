import sys

input = sys.stdin.readline

N = int(input())

arr = [*map(int, input().split())]
inc = [1 for _ in range(N)]
dec = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            inc[i] = max(inc[i], inc[j] + 1)
    for j in range(N - 1, N - i - 1, -1):
        if arr[j] < arr[N - i - 1]:
            dec[N - i - 1] = max(dec[N - i - 1], dec[j] + 1)

res = 0
for a, b in zip(inc, dec):
    if res < a + b:
        res = a + b
print(res - 1)