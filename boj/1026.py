import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B.sort()
A.sort(reverse=True)

print(sum([A[i] * B[i] for i in range(N)]))
