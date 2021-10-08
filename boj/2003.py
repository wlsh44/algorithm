import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split())) + [0]

cnt = 0
sum_ = 0
i, j = 0, 0
while j <= N:
    if sum_ < M:
        sum_ += arr[j]
        j += 1
    else:
        sum_ -= arr[i]
        i += 1
    if sum_ == M:
        cnt += 1
print(cnt)