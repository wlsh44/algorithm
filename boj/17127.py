N = int(input())

arr = list(map(int, input().split()))

res = 0

for i in range(1, N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            num1 = 1
            for t in range(i):
                num1 *= arr[t]
            num2 = 1
            for t in range(i, j):
                num2 *= arr[t]
            num3 = 1
            for t in range(j, k):
                num3 *= arr[t]
            num4 = 1
            for t in range(k, N):
                num4 *= arr[t]
            res = max(res, num1 + num2 + num3 + num4)

print(res)
