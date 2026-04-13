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

# ---

# 한 세트 0~9

N = input()
count = [0] * 10

for c in N:
    count[int(c)] += 1

tmp = count[6] + count[9]
count[6] = tmp // 2 if tmp % 2 == 0 else tmp // 2 + 1
count[9] = 0
print(max(count))
