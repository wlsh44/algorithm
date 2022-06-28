N = int(input())

arr = []
for _ in range(N):
    tmp = input().split()

    arr.append((tmp[0], int(tmp[1])))

arr.sort(key=lambda x: x[1])

for x in arr:
    print(x[0], end=" ")
