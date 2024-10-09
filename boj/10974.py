from itertools import permutations

N = int(input())

arr = [i for i in range(1, N + 1)]

perms = permutations(arr, N)

for perm in perms:
    print(*perm)
