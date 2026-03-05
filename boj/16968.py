arr = list(input())

num = 10 if arr[0] == 'd' else 26
ans = num
for i in range(1, len(arr)):
    if arr[i - 1] == arr[i]:
        num = 9 if arr[i] == 'd' else 25
    else:
        num = 10 if arr[i] == 'd' else 26
    ans *= num
print(ans)
