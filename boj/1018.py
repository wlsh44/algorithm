N, M = map(int, input().split())

chess = [input() for _ in range(N)]
ans = 10e9


def paint(i, j):
    c1 = 'W'
    c2 = 'B'
    cnt1 = 0
    cnt2 = 0
    for y in range(i, i + 8):
        for x in range(j, j + 8):
            if chess[y][x] != c1:
                cnt1 += 1
            if chess[y][x] != c2:
                cnt2 += 1
            c1 = 'W' if c1 == 'B' else 'B'
            c2 = 'W' if c2 == 'B' else 'B'
        c1 = 'W' if c1 == 'B' else 'B'
        c2 = 'W' if c2 == 'B' else 'B'
    return min(cnt1, cnt2)

for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        ans = min(ans, paint(i, j))
print(ans)
