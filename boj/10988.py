s = list(input())

for i in range(len(s) // 2 + 1):
    if s[i] != s[len(s) - 1 - i]:
        print(0)
        exit()
print(1)