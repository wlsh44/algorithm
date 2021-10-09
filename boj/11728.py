import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

arr = sorted(A + B)
for i in arr:
    print(i, end=" ")

