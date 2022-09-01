N, M = map(int, input().split())

arr = [int(input()) for _ in range(N)]

left, right = 1, max(arr)

res = 0
while left <= right:
    mid = (left + right) // 2

    tmp = sum([x // mid for x in arr])
    if tmp >= M:
        left = mid + 1
        res = mid
    else:
        right = mid - 1
print(res)
