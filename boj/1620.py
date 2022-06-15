import sys

input = sys.stdin.readline

N, M = map(int, input().split())

name_num = {input().rstrip(): v for v in range(1, N + 1)}
num_name = {v + 1: k for v, k in enumerate(name_num)}

for _ in range(M):
    string = input().rstrip()
    if string.isdigit():
        print(num_name[int(string)])
    else:
        print(name_num[string])
