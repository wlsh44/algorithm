key = list(input())
pwd = list(input())

arr = [[c, [], False] for c in sorted(key)]
for i in range(len(pwd)):
    arr[i // (len(pwd) // len(key))][1].append(pwd[i])

ans = []
for c in key:
    for i in range(len(arr)):
        if c == arr[i][0] and arr[i][2] is False:
            arr[i][2] = True
            ans.append(arr[i][1])
            break

for i in range(len(ans[0])):
    for j in range(len(ans)):
        print(ans[j][i], end="")