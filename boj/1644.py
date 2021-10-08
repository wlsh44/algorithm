N = int(input())

check = [False, False] + [True] * N
primes = []
for i in range(2, N + 1):
    if check[i]:
        primes.append(i)
        for j in range(i * 2, N + 1, i):
            check[j] = False

primes += [0]
i, j = 0, 0
sum_ = 0
cnt = 0
while j < len(primes):
    if sum_ < N:
        sum_ += primes[j]
        j += 1
    else:
        sum_ -= primes[i]
        i += 1
    if sum_ == N:
        cnt += 1
print(cnt)