import sys

input = sys.stdin.readline

N = int(input())
card = set(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))

for i in arr:
    res = 1 if i in card else 0
    print(res, end=" ")
