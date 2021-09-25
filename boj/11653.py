N = int(input())

arr = [False, False] + [True] * N
primes = []
for i in range(1, N + 1):
    if arr[i]:
        primes.append(i)
        for j in range(i * 2, N + 1, i):
            arr[j] = False

if N != 0:
    for prime in primes:
        while N % prime == 0:
            print(prime)
            N //= prime
