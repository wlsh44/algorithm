A = [list(map(int, input().split())) for _ in range(5)]
B = [list(map(int, input().split())) for _ in range(5)]

res = 10e9
ans = 0

for x in range(5):
    tmp = 0
    for y in range(5):
        for i in range(5):
            tmp += A[x][i] * B[i][y]
    if tmp <= res:
        res = tmp
        ans = x

print(["Inseo", "Junsuk", "Jungwoo", "Jinwoo", "Youngki"][ans])
