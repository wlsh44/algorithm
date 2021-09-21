import sys

input = sys.stdin.readline
s1 = list(input().strip())
s2 = []
N = int(input())
for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'L':
        if s1:
            s2.append(s1.pop())
    elif cmd[0] == 'D':
        if s2:
            s1.append(s2.pop())
    elif cmd[0] == 'B':
        if s1:
            s1.pop()
    elif cmd[0] == 'P':
        s1.append(cmd[1])
print("".join(s1 + list(reversed(s2))))
