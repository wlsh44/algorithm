N = int(input())
arr = list(map(int, input().split()))

start = arr[0]
ans = 0
for i in range(1, N):
    if arr[i] <= arr[i - 1]:
        start = arr[i]
    else:
        ans = max(ans, arr[i] - start)
print(ans)
