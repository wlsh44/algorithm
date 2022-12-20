import sys
from collections import deque

input = sys.stdin.readline
T = int(input())


def bfs(A, B):
    nums = {A}
    q = deque([(A, "")])

    while q:
        num, cmd = q.popleft()
        if num == B:
            return cmd

        num_D = (num * 2) % 10000
        cmd_D = cmd + "D"
        if num_D not in nums:
            nums.add(num_D)
            q.append((num_D, cmd_D))

        num_S = num - 1 if num != 0 else 9999
        cmd_S = cmd + "S"
        if num_S not in nums:
            nums.add(num_S)
            q.append((num_S, cmd_S))

        num_L = (10 * num + (num // 1000)) % 10000
        cmd_L = cmd + "L"
        if num_L not in nums:
            nums.add(num_L)
            q.append((num_L, cmd_L))

        num_R = (num // 10 + (num % 10) * 1000) % 10000
        cmd_R = cmd + "R"
        if num_R not in nums:
            nums.add(num_R)
            q.append((num_R, cmd_R))


for _ in range(T):
    A, B = map(int, input().split())

    print(bfs(A, B))
