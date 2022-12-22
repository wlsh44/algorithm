import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())

    clothes_map = {}
    for _ in range(n):
        clothes, kinds = input().split()
        clothes_map.setdefault(kinds, 1)
        clothes_map[kinds] += 1

    res = 1
    for cnt in clothes_map.values():
        res *= cnt
    print(res - 1 if n != 0 else 0)
