import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())

r, c, d = map(int, input().split())

m = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def turn_left(vec):
    return vec - 1 if vec - 1 >= 0 else 3


def clean(y, x, vec, cnt, res):
    back = turn_left(turn_left(vec))
    if cnt == 4:
        if m[dy[back] + y][dx[back] + x] == 1:
            print(res)
            return
        clean(dy[back] + y, dx[back] + x, vec, 0, res)
    else:
        m[y][x] = 2
        new_vec = turn_left(vec)
        if m[dy[new_vec] + y][dx[new_vec] + x] == 0:
            clean(y + dy[new_vec], x + dx[new_vec], new_vec, 0, res + 1)
        elif m[dy[new_vec] + y][dx[new_vec]] == 1 or 2:
            clean(y, x, new_vec, cnt + 1, res)


clean(r, c, d, 0, 1)
