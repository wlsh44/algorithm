arr = [False] * 31

for _ in range(28):
    n = int(input())
    arr[n] = True

res = []
for i in range(1, 31):
    if not arr[i]:
        res.append(i)

res.sort()
print(res[0])
print(res[1])