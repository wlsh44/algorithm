# from itertools import permutations
# from collections import deque
#
# N = int(input())
#
# exp = list(map(int, input().split()))
# op_nums = list(map(int, input().split()))
# ops = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x // y if x > 0 else -(-x // y)]
#
# arr = []
# for op, num in zip(ops, op_nums):
#     for _ in range(num):
#         arr.append(op)
#
# op_perm = permutations(arr)
#
# res = []
# for op_p in op_perm:
#     op_p = deque(op_p)
#     tmp = deque(exp.copy())
#     while op_p:
#         op = op_p.popleft()
#         x = tmp.popleft()
#         y = tmp.popleft()
#         tmp.appendleft(op(x, y))
#     res.append(tmp.pop())
# print(max(res))
# print(min(res))

N = int(input())

exp = list(map(int, input().split()))
op = list(map(int, input().split()))
res = []


def dfs(total, i, p, s, m, d):
    if i == N:
        res.append(total)
        return

    if p:
        dfs(total + exp[i], i + 1, p - 1, s, m, d)
    if s:
        dfs(total - exp[i], i + 1, p, s - 1, m, d)
    if m:
        dfs(total * exp[i], i + 1, p, s, m - 1, d)
    if d:
        dfs(int(total / exp[i]), i + 1, p, s, m, d - 1)


dfs(exp[0], 1, op[0], op[1], op[2], op[3])
print(max(res))
print(min(res))
