import sys
from collections import deque


input = sys.stdin.readline
T = int(input())

for _ in range(T):
    arr = list(input().strip())

    s = []
    q = deque([])
    for c in arr:
        if c == "<":
            if not s:
                continue
            q.appendleft(s.pop())
        elif c == ">":
            if not q:
                continue
            s.append(q.popleft())
        elif c == "-":
            if not s:
                continue
            s.pop()
        else:
            s.append(c)
    print("".join(s) + "".join(q))

# ---
from collections import deque

T = int(input())

for _ in range(T):
    arr = input()
    s1 = []
    s2 = deque([])
    for c in arr:
        if c == '<':
            if s1:
                s2.appendleft(s1.pop())
        elif c == '>':
            if s2:
                s1.append(s2.popleft())
        elif c == '-':
            if s1:
                s1.pop()
        else:
            s1.append(c)
    print(''.join(s1) + ''.join(s2))
