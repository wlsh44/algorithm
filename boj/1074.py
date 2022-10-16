import sys

sys.setrecursionlimit(1000000)
N, r, c = map(int, input().split())

res = 0


def visit_z(start_r, end_r, start_c, end_c):
    global res
    for i in range(start_r, end_r + 1):
        for j in range(start_c, end_c + 1):
            if i == r + 1 and j == c + 1:
                print(res)
            res += 1


def rec(start_r, end_r, start_c, end_c):
    global res
    if not (start_r <= r + 1 <= end_r and start_c <= c + 1 <= end_c):
        res += (end_r - start_r + 1) * (end_c - start_c + 1)
        return
    if end_r - start_r == 1:
        visit_z(start_r, end_r, start_c, end_c)
        return

    mid_r = (start_r + end_r) // 2
    mid_c = (start_c + end_c) // 2
    rec(start_r, mid_r, start_c, mid_c)
    rec(start_r, mid_r, mid_c + 1, end_c)
    rec(mid_r + 1, end_r, start_c, mid_c)
    rec(mid_r + 1, end_r, mid_c + 1, end_c)


rec(1, pow(2, N), 1, pow(2, N))
