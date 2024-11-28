n = int(input())
s = input()

arr = [0] * (len(s) + 1)
for i in range(1, len(s) + 1):
    arr[i] = arr[i - 1] + i
ans = 0

i = 0
while i < len(s):
    cnt = 0
    while i < len(s) and s[i] == '2':
        cnt += 1
        ans += arr[cnt]
        i += 1
    i += 1
print(ans)

222
1 + (1 + 2) + (1 + 2 + 3)

22
1 + (1 + 2)

2
1