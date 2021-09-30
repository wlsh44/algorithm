import sys


def check(arr, m):
    res = 0
    sum_ = 0
    for time in arr:
        if time > m:
            return sys.maxsize
        if sum_ + time <= m:
            sum_ += time
        else:
            sum_ = time
            res += 1
    return res + 1


input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
l, r = 0, sum(arr)
res = 0

while l <= r:
    m = (l + r) // 2
    if check(arr, m) <= M:
        res = m
        r = m - 1
    else:
        l = m + 1
print(res)
