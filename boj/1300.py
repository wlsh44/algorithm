N = int(input())
k = int(input())

mid = 0
left, right = 1, N * N

res = 0
while left <= right:
    mid = (left + right) // 2

    tmp = sum([min(mid // i, N) for i in range(1, N + 1)])
    print(f"left {left} right {right} tmp {tmp}")

    if tmp >= k:
        right = mid - 1
        res = mid
    else:
        left = mid + 1
print(res)

# 1 2 3 4
# 2 4 6 8
# 3 6 9 12
# 4 8 12 16
#
# 1~16 임의의 값
# 1~4의 배수