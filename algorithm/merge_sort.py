def merge_sort(arr, left, right):
    if right - left <= 1:
        return

    mid = (left + right) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid, right)
    merge(arr, left, mid, right)


def merge(arr, left, mid, right):
    tmp = []
    l, r = left, mid
    while l < mid and r < right:
        if arr[l] <= arr[r]:
            tmp.append(arr[l])
            l += 1
        else:
            tmp.append(arr[r])
            r += 1
    while l < mid:
        tmp.append(arr[l])
        l += 1
    while r < right:
        tmp.append(arr[r])
        r += 1
    arr[left:right] = tmp


arr = [7, 5, 9, 0, 3, 1, 1, 6, 2, 4, 8]

merge_sort(arr, 0, len(arr))
print(arr)