import sys

input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x : (x[1], x[0]))
for s in arr:
	print(f"{s[0]} {s[1]}")