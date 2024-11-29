from itertools import permutations

N = int(input())
ans = 0
bulbs = []
for _ in range(N):
    s = input()
    ans += s.count("10") + s.count("01")
    bulbs.append(s[0] + s[-1])

perm = permutations(bulbs)

cnt = 10e9
for p in perm:
    tmp = 0
    for i in range(N - 1):
        if p[i][1] != p[i + 1][0]:
            tmp += 1
    cnt = min(cnt, tmp)
print(ans + cnt)
