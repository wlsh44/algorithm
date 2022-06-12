N = int(input())
move = list(map(str, input().split()))

cur = [1, 1]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for m in move:
    if m == "D":
        vec = 0
    elif m == "R":
        vec = 1
    elif m == "U":
        vec = 2
    else:
        vec = 3
    x = cur[1] + dx[vec]
    y = cur[0] + dy[vec]
    if not (y > N or y <= 0 or x > N or x <= 0):
        cur[1] = x
        cur[0] = y

print(f"{cur[0]} {cur[1]}")