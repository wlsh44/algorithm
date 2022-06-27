arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[right], arr[left] = arr[left], arr[right]

    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


quick_sort(arr, 0, len(arr) - 1)
print(arr)


def quick_sort2(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    tail = arr[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quick_sort2(left) + [pivot] + quick_sort2(right)


print(quick_sort2(arr))
