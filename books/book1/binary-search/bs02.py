def bs(target, arr):
    left = 0
    right = len(arr)

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return True
    return False


N = int(input())
prod = list(map(int, input().split()))
M = int(input())
orders = list(map(int, input().split()))

prod.sort()

for order in orders:
    res = bs(order, prod)
    if res:
        print("yes", end=" ")
    else:
        print("no", end=" ")
