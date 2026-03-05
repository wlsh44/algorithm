import sys

input = sys.stdin.readline

n, m = map(int, input().split())

switches = [set(list(map(int, input().split()))[1:]) for _ in range(n)]
ramp = [False for _ in range(m)]

flag = False
for i in range(n):
    res = set()
    for j in range(n):
        if i == j:
            continue
        for num in switches[j]:
            res.add(num)
    if len(res) == m:
        flag = True
        break
print(1 if flag else 0)
