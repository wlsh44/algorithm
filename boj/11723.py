import sys

input = sys.stdin.readline

s = [0] * 21

M = int(input())

for _ in range(M):
    cmd = input().rstrip()

    if cmd == "all":
        s = [1] * 21
    elif cmd == "empty":
        s = [0] * 21
    else:
        cmd, num = cmd.split()
        num = int(num)
        if cmd == "add":
            s[num] = 1
        elif cmd == "remove":
            s[num] = 0
        elif cmd == "check":
            print(s[num])
        elif cmd == "toggle":
            s[num] = 1 if s[num] == 0 else 0

