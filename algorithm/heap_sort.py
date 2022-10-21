def heapify(arr, i, size):
    left = i * 2 + 1
    right = i * 2 + 2
    parent = i
    if left < size and arr[i] < arr[left]:
        i = left
    if right < size and arr[i] < arr[right]:
        i = right
    if parent != i:
        arr[parent], arr[i] = arr[i], arr[parent]
        heapify(arr, i, size)


arr = [1, 7, 6, 2, 4, 3, 5, 2, 1, 9]
for i in range(len(arr) // 2 - 1, -1, -1):
    heapify(arr, i, len(arr))
    print(arr)

print()
for i in range(len(arr) - 1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]
    heapify(arr, 0, i)

print(arr)