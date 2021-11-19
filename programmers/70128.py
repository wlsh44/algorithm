def solution(a, b):
    if len(a) == 0:
        return 0
    return sum([num1 * num2 for num1, num2 in zip(a, b)])