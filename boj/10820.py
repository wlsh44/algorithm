import sys

input = sys.stdin.readline
while 1:
    low, up, space, num = 0, 0, 0, 0
    s = input().rstrip('\n')
    if not s:
        break
    for c in s:
        if c.isupper():
            up += 1
        elif c.islower():
            low += 1
        elif c.isnumeric():
            num += 1
        elif c.isspace():
            space += 1
    print(low, up, num, space)

