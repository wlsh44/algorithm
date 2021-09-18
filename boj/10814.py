import sys

input = sys.stdin.readline
N = int(input())
arr = []
for i in range(N):
	arr.append(list(input().split()))

arr.sort(key=lambda x : int(x[0]))

for i in arr:
	print(i[0], i[1])