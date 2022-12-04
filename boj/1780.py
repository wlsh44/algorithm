import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
res = {-1: 0, 0: 0, 1: 0}


def check_same_number(end_x, end_y, number, start_x, start_y):
    for i in range(start_y, end_y + 1):
        for j in range(start_x, end_x + 1):
            if paper[i][j] != number:
                return False
    return True


def rec(start_y, start_x, end_y, end_x):
    number = paper[start_y][start_x]

    if not check_same_number(end_x, end_y, number, start_x, start_y):
        paper_size = (end_y - start_y + 1) // 3
        if paper_size == 0:
            res[number] += 1
            return
        for i in range(start_y, end_y + 1, paper_size):
            for j in range(start_x, end_x + 1, paper_size):
                rec(i, j, i + paper_size - 1, j + paper_size - 1)
    else:
        res[number] += 1


rec(0, 0, N - 1, N - 1)
print(res[-1], res[0], res[1], sep="\n")