import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

left, right = 0, len(arr) - 1
arr.sort()
ans = 0
while left < right:
    if arr[left] + arr[right] > x:
        right -= 1
    elif arr[left] + arr[right] < x:
        left += 1
    else:
        ans += 1
        left += 1
print(ans)
