import sys

input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split())) + [0]

i, j = 0, 0
sum_ = 0
res = sys.maxsize
while j <= N:
    if sum_ < S:
        sum_ += arr[j]
        j += 1
    else:
        sum_ -= arr[i]
        i += 1
    if sum_ >= S:
        res = min(res, j - i)
print(res if res != sys.maxsize else 0)