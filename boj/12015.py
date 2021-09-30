from bisect import bisect_left
import sys

input = sys.stdin.readline
N = int(input())
s = list(map(int, input().split()))

lis = [0]
dp = [0]
idx = 0
for num in s:
    idx = bisect_left(lis, num)
    if idx == len(lis) - 1:
        lis.append(lis(idx) + 1)
        dp
    else:

