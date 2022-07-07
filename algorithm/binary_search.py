def binary_search(target, arr):
    left = 0
    right = len(arr)

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] == target:
            return mid
        else:
            right = mid - 1
    return None


arr = [1, 3, 4, 6, 7, 9, 10]
print(binary_search(4, arr))
print(binary_search(5, arr))
