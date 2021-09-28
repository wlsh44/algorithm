def binary_search(target, arr):
    l, r = 0, len(arr) - 1

    while l <= r:
        m = (r + l) // 2
        if arr[m] < target:
            l = m + 1
        elif arr[m] > target:
            r = m - 1
        else:
            return True
    return False


N = int(input())
arr = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

arr.sort()
for target in arr2:
    print(1) if binary_search(target, arr) else print(0)
