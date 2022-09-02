N = int(input())
k = int(input())

mid = 0
left, right = 1, N * N

while left <= right:
    mid = (left + right) // 2

    tmp = sum([min(mid // i, N) for i in range(1, N + 1)])

    if tmp >= k:
        right = mid - 1
    else:
        left = mid + 1
print(mid)
