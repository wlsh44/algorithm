N, M = map(int, input().split())

height = list(map(int, input().split()))


def bs(target):
    arr = [i for i in range(max(height) - M, max(height) + 1)]
    left, right = 0, len(height)
    res = 0

    while left <= right:
        mid = (left + right) // 2

        tmp = sum([x - arr[mid] for x in height if x > arr[mid]])
        if tmp < target:
            right = mid - 1
        elif tmp > target:
            left = mid + 1
            res = tmp
        else:
            res = tmp
            break
    return res


print(bs(M))
