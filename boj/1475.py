s = list(input())

arr = [0] * 9
res = 0
for c in s:
    num = int(c)
    if num == 9:
        num = 6
    if arr[num] == 0:
        for i in range(9):
            arr[i] += 1
        arr[6] += 1
        res += 1
    arr[num] -= 1
print(res)