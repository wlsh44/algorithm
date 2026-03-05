while True:
    try:
        s, t = map(list, input().split())

        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j += 1
                i += 1
            else:
                j += 1

        print("Yes" if i == len(s) else "No")
    except:
        exit()