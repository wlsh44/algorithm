N = int(input())

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

arr = [list(input()) for _ in range(N)]

def count(i, j):
    ans = 0
    ans1 = 0
    ans2 = 0
    row_cnt = 1
    col_cnt = 1
    for k in range(1, N):
        if arr[i][k - 1] == arr[i][k]:
            col_cnt += 1
        else:
            ans1 = max(ans1, col_cnt)
            col_cnt = 1
        if arr[k - 1][j] == arr[k][j]:
            row_cnt += 1
        else:
            ans2 = max(ans2, row_cnt)
            row_cnt = 1
    ans = max(ans1, ans2, row_cnt, col_cnt)
    return ans


ans = 0

for i in range(N):
    for j in range(N):
        for dy, dx in d:
            if 0 <= dy + i < N and 0 <= dx + j < N:
                arr[i][j], arr[dy + i][dx + j] = arr[dy + i][dx + j], arr[i][j]
                ans = max(ans, count(i, j))
                arr[i][j], arr[dy + i][dx + j] = arr[dy + i][dx + j], arr[i][j]

print(ans)
