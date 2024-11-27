m, seed, x1, x2 = map(int, input().split())

for a in range(m):
    if ((x2 - x1) + (seed - x1) * a) % m != 0:
        continue
    for c in range(m):
        if x1 == (a * seed + c) % m and x2 == (a * x1 + c) % m:
            print(a, c)
            exit()
