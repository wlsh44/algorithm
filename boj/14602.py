N, M, K, W = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

ans = [[] for _ in range(N - W + 1)]
for i in range(N - W + 1):
    for j in range(M - W + 1):
        tmp = []
        for y in range(i, i + W):
            for x in range(j, j + W):
                tmp.append(arr[y][x])
        tmp.sort()
        ans[i].append(tmp[len(tmp) // 2])
for row in ans:
    print(*row)
