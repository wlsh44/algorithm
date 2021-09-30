import sys


def count(arr, m):
    cur, cnt = 0, 0
    for money in arr:
        if cur < money:
            cur = m
            cnt += 1
        cur -= money
    return cnt


input = sys.stdin.readline
N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

l, r = min(arr), sum(arr)

ans = 0
while l <= r:
    m = (r + l) // 2
    if count(arr, m) <= M and m >= max(arr):
        ans = m
        r = m - 1
    else:
        l = m + 1
print(ans)
