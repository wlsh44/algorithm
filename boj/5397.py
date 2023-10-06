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