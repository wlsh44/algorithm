N = int(input())
M = int(input())

arr = list(map(int, input().split()))

arr.sort()

left, right = 0, len(arr) - 1

ans = 0
while left < right:
    if arr[left] + arr[right] > M:
        right -= 1
    elif arr[left] + arr[right] < M:
        left += 1
    else:
        ans += 1
        left += 1

print(ans)
