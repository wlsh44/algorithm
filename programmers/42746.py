from functools import cmp_to_key


def func(a, b):
    return -(int(a + b) - int(b + a))


def solution(numbers):
    if all([num == 0 for num in numbers]):
        return "0"
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(func))
    # answer = str(int(''.join(numbers)))
    answer = ''.join(numbers)
    return answer