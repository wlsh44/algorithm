arr = list(input())
s = []
tmp = 1
ans = 0
for i in range(len(arr)):
    if arr[i] == '(':
        s.append(arr[i])
        tmp *= 2
    elif arr[i] == '[':
        s.append(arr[i])
        tmp *= 3
    elif arr[i] == ')':
        if not s or s[-1] != '(':
            print(0)
            exit()
        if arr[i - 1] == '(':
            ans += tmp
        s.pop()
        tmp //= 2
    elif arr[i] == ']':
        if not s or s[-1] != '[':
            print(0)
            exit()
        if arr[i - 1] == '[':
            ans += tmp
        s.pop()
        tmp //= 3
if s:
    print(0)
else:
    print(ans)