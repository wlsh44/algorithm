x, y = map(int, input().split())

z = int(y / x * 100)

if z >= 99:
    print(-1)
else:
    left, right = 1, x

    mid = (left + right) // 2
    ans = 0
    while left <= right:
        mid = (left + right) // 2

        if z == (y + mid) * 100 // (x + mid):
            left = mid + 1
        else:
            right = mid - 1
            ans = mid
    print(ans)
