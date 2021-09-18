import sys

N = int(input())

arr = []

for i in range(N):
	arr.append(int(sys.stdin.readline().rstrip()))

arr.sort()

for num in arr:
	print(num)