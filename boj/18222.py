k = int(input())

arr = []
for i in range(k):
    if 2 ** i > k:
        break
    arr.append(2 ** i)

num = arr.pop()
while k != 0 and k != 1 and k != 2:
    while num > k:
        num = arr.pop()
    k -= num
    print(k)
if k == 0 or k == 2:
    print(0)
else:
    print(1)