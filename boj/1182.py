from itertools import combinations

N, S = map(int, input().split())

arr = list(map(int, input().split()))

res = 0

for i in range(1, N + 1):
	for comb in combinations(arr, i):
		if sum(comb) == S:
			res += 1
print(res)