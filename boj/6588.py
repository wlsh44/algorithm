import sys

n = 1000001
input = sys.stdin.readline
primes = [False, False] + [True] * (n - 1)
for i in range(2, n + 1):
    if primes[i]:
        for j in range(i * 2, n + 1, i):
            primes[j] = False
while True:
    N = int(input())
    if N == 0:
        break
    flag = False
    for i in range(3, len(primes)):
        if primes[i] and primes[N - i]:
            print(f"{N} = {i} + {N - i}")
            flag = True
            break
    if not flag:
        print("Goldbach's conjecture is wrong.")