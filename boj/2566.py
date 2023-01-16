arr = [list(map(int, input().split())) for _ in range(9)]

res = 0
y, x = 0, 0
for i in range(9):
    for j in range(9):
        if res < arr[i][j]:
            res = arr[i][j]
            y, x = i, j
print(res)
print(y + 1, x + 1)