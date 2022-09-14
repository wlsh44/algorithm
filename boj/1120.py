str1, str2 = map(list, input().split())

res = []
for start in range(len(str2) - len(str1) + 1):
    cnt = 0
    for j in range(len(str1)):
        if str1[j] != str2[start + j]:
            cnt += 1
    res.append(cnt)
print(min(res))