N, M = map(int, input().split())

arr = [i for i in range(1, N + 1)]

for _ in range(M):
    i, j = map(int, input().split())

    k = 0
    for idx in range(i, (j + i) // 2 + 1):
        arr[idx - 1], arr[j - k - 1] = arr[j - k - 1], arr[idx - 1]
        k += 1
print(*arr)
