from itertools import combinations

arr = [int(input()) for _ in range(9)]

comb = combinations(arr, 7)
for c in comb:
    if sum(c) == 100:
        c = list(c)
        c.sort()
        for x in c:
            print(x)
        break
