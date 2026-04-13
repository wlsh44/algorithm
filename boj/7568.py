N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
ans = [0 for _ in range(N)]
for i in range(N):
    ans[i] = 1
    for j in range(N):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            ans[i] += 1
print(*ans)
