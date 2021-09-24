import sys
from itertools import combinations
from math import gcd

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    ans = 0
    arr = list(map(int, input().split()))
    combs = list(combinations(arr[1:], 2))
    for comb in combs:
        ans += gcd(comb[0], comb[1])
    print(ans)