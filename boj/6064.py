import sys

input = sys.stdin.readline
T = int(input())


def solve():
    M, N, x, y = map(int, input().split())
    while x <= N * M:
        if x % N == y % N:
            return x
        x += M
    return -1


for _ in range(T):
    print(solve())