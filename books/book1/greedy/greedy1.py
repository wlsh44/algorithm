import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort(reverse=True)
ans = 0

"""answer1"""
for i in range(1, M + 1):
    if i % (K + 1) == 0:
        ans += arr[1]
    else:
        ans += arr[0]
print(ans)

"""answer2"""
cnt = M // (K + 1)

ans = (M // (K + 1)) * (arr[0] * K + arr[1]) + (M % (K + 1)) * arr[0]
print(ans)

