import sys

input = sys.stdin.readline

N, M = map(int, input().split())
ans = 0
for _ in range(N):
    arr = list(map(int, input().split()))
    ans = max(min(arr), ans)
print(ans)

