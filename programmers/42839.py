from itertools import permutations

def get_primes(length):
    primes = [False, False] + [True] * length
    for i in range(2, length + 1):
        if primes:
            for j in range(i * 2, length + 1, i):
                primes[j] = False
    return primes

def solution(numbers):
    answer = 0
    comb = []
    for r in range(1, len(numbers) + 1):
        comb += list(permutations(numbers, r))
    comb = [int(''.join(num)) for num in comb]
    comb = list(set(comb))
    length = max(comb)
    primes = get_primes(length)
    for num in comb:
        if primes[num]:
            answer += 1
    return answer