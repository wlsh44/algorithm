arr = []
for i in range(5):
    arr.append([None] * 15)
    row = list(input())
    for j in range(len(row)):
        arr[i][j] = row[j]

for i in range(15):
    for j in range(5):
        if arr[j][i] == None:
            continue
        print(arr[j][i], end="")