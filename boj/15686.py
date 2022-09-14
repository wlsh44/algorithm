from itertools import combinations

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            houses.append((i, j))
        elif arr[i][j] == 2:
            chickens.append((i, j))

combs = list(combinations(chickens, M))
res = []
for comb in combs:
    total_dist = 0
    for house in houses:
        min_dist = N * N
        y, x = 0, 0
        for chicken in comb:
            dy, dx = abs(chicken[0] - house[0]), abs(chicken[1] - house[1])
            if dy + dx < min_dist:
                y, x = dy, dx
                min_dist = dy + dx
        total_dist += min_dist
    res.append(total_dist)
print(min(res))
