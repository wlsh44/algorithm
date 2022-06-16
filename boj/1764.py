import sys

input = sys.stdin.readline

N, M = map(int, input().split())

listen = {input() for _ in range(N)}
see = {input() for _ in range(M)}

res = listen & see
res = sorted(res)
print(len(res))
for name in res:
    print(name)
