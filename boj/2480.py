arr = list(map(int, input().split()))

arr.sort(reverse=True)
if arr[0] == arr[1] and arr[1] == arr[2]:
    print(arr[1] * 1000 + 10000)
elif arr[0] == arr[1] or arr[1] == arr[2]:
    print(arr[1] * 100 + 1000)
else:
    print(arr[0] * 100)
