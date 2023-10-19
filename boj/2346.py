import sys
from collections import deque


input = sys.stdin.readline
N = int(input())

q = deque(enumerate(map(int, input().split())))

res = []
while q:
    idx, num = q.popleft()
    res.append(idx + 1)
    if num > 0:
        q.rotate(-(num - 1))
    else:
        q.rotate(-num)
print(*res)