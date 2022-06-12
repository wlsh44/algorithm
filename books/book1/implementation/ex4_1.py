N = int(input())
move_arr = list(map(str, input().split()))

nx, ny = 1, 1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
move = ["D", "R", "U", "L"]
for vec in move_arr:
    for i in range(len(move)):
        if vec == move[i]:
            x, y = nx + dx[i], ny + dy[i]
    if not (y > N or y <= 0 or x > N or x <= 0):
        nx, ny = x, y
print(f"{ny} {nx}")
