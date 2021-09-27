N = int(input())

num = N
for prime in range(2, N + 1):
    if num == 1:
        break
    while num % prime == 0:
        print(prime)
        num /= prime
