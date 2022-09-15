string = list(input())

arr = []
i = 0
while i < len(string):
    if string[i] == "<":
        start = i
        while string[i] != ">":
            i += 1
        i += 1
        arr.append(''.join(string[start:i]))
    else:
        start = i
        while i < len(string) and string[i] != "<":
            i += 1
        tmp = "".join(string[start:i]).split()
        s = []
        for c in tmp:
            s.append(''.join(reversed(c)))
        arr.append(" ".join(s))
print(''.join(arr))