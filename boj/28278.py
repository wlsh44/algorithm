import sys


input = sys.stdin.readline

N = int(input())

s = []
for _ in range(N):
    cmd = input()
    a = int(list(cmd)[0])
    b = None

    if a == 1:
        _, b = map(int, cmd.split())
        s.append(b)
    elif a == 2:
        if s:
            print(s.pop())
        else:
            print(-1)
    elif a == 3:
        print(len(s))
    elif a == 4:
        print(0 if s else 1)
    else:
        if s:
            print(s[-1])
        else:
            print(-1)