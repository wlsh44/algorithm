from itertools import combinations


N = int(input())

d = {i: list(map(int, input().split())) for i in range(1, N + 1)}

ans = []
for num, arr in d.items():
    comb = combinations(arr, 3)

    res = [0, num]
    for c in comb:
        res[0] = max(sum(c) % 10, res[0])
    ans.append(res)

ans.sort(key=lambda x: (-x[0], -x[1]))
print(ans[0][1])
