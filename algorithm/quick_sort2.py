def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[(len(arr)) // 2]

    lesser, same, larger = [], [], []
    for num in arr:
        if num < pivot:
            lesser.append(num)
        elif num == pivot:
            same.append(num)
        else:
            larger.append(num)

    return quick_sort(lesser) + same + quick_sort(larger)


arr = [7, 5, 9, 0, 3, 1, 1, 6, 2, 4, 8]

print(quick_sort(arr))


def quick_sort2(arr, start, end):
    if start >= end:
        return

    left = start
    right = end
    pivot = arr[(left + right) // 2]
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left, right = left + 1, right - 1
    mid = left
    quick_sort2(arr, start, mid - 1)
    quick_sort2(arr, mid, end)


arr = [7, 5, 9, 0, 3, 1, 1, 6, 2, 4, 8]
quick_sort2(arr, 0, len(arr) - 1)
print(arr)