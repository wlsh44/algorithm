from itertools import permutations

N = int(input())

w = [list(map(int, input().split())) for _ in range(N)]
perms = permutations(range(N), N)
ans = 10e9
for perm in perms:
    res = 0
    flag = False
    for i in range(N):
        cur = perm[i]
        next = perm[0] if i + 1 == N else perm[i + 1]
        cost = w[cur][next]
        if cost == 0:
            flag = True
            break
        res += cost
    if flag:
        continue
    ans = min(ans, res)
print(ans)
