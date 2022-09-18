from itertools import permutations
from collections import deque

N = int(input())

exp = list(map(int, input().split()))
op_nums = list(map(int, input().split()))
ops = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x // y if x > 0 else -(-x // y)]

arr = []
for op, num in zip(ops, op_nums):
    for _ in range(num):
        arr.append(op)

op_perm = permutations(arr)

res = []
for op_p in op_perm:
    op_p = deque(op_p)
    tmp = deque(exp.copy())
    while op_p:
        op = op_p.popleft()
        x = tmp.popleft()
        y = tmp.popleft()
        tmp.appendleft(op(x, y))
    res.append(tmp.pop())
print(max(res))
print(min(res))