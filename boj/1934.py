import sys
from math import lcm

input = sys.stdin.readline
N = int(input())

for _ in range(N):
    A, B = map(int, input().split())
    print(lcm(A, B))

