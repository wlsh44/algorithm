s = input()
for c in s:
    if c.isalpha():
        if (c >= 'A' and c <= 'M') or (c >= 'a' and c <= 'm'):
            print(chr(ord(c) + 13), end='')
        else:
            print(chr(ord(c) - 13), end='')
    else:
        print(c, end='')
