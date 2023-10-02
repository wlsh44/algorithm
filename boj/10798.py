N = int(input())

arr = [i for i in range(4)]
for _ in range(N):
    a, b = map(int, input().split())
    i1 = arr.index(a)
    i2 = arr.index(b)
    arr[i1], arr[i2] = b, a
print(arr[1])
