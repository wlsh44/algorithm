s = input()
arr = []
for i in range(len(s)):
    arr.append(s[i:]) == arr.append(s[0:])
arr.sort()
for baum in arr:
    print(baum)
