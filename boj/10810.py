N, M = map(int, input().split())

arr = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    for idx in range(i, j + 1):
        arr[idx - 1] = k
print(*arr)