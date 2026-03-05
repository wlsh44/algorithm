import math


def solution(r1, r2):
    answer = 0;
    big, small, line = 0, 0, 0

    cnt = 0
    for i in range(1, r2):
        cnt = int(math.sqrt(r2 ** 2 - i ** 2))
        big += cnt

    cnt = 0
    for i in range(1, r1):
        num = math.sqrt(r1 ** 2 - i ** 2)
        cnt = int(num)
        if num - cnt == 0:
            cnt -= 1
        small += cnt

    line = r2 - r1 + 1
    return (big - small + line) * 4