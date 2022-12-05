import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())

video = [list(input()) for _ in range(N)]
ans = []


def is_same_color(e_x, e_y, s_x, s_y, symbol):
    for i in range(s_y, e_y):
        for j in range(s_x, e_x):
            if video[i][j] != symbol:
                return False
    return True


def rec(start, end):
    s_y, s_x = start
    e_y, e_x = end
    symbol = video[s_y][s_x]

    if e_y - s_y == 1:
        ans.append(str(symbol))
        return

    if is_same_color(e_x, e_y, s_x, s_y, symbol):
        ans.append(str(symbol))
    else:
        ans.append("(")
        step = (e_y - s_y) // 2
        for i in range(s_y, e_y, step):
            for j in range(s_x, e_x, step):
                rec((i, j), (i + step, j + step))
        ans.append(")")


rec((0, 0), (N, N))
print("".join(ans))
