from itertools import combinations

def solution(numbers):
    comb = combinations(numbers, 2)
    return sorted(list(set(map(sum, comb))))