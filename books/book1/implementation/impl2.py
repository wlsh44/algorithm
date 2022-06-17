pos = input()

dx = [2, 2, -2, -2, 1, -1]
dy = [1, -1, 1, -1, 2, -2]

res = 0
x = ord(pos[0]) - ord('a') + 1
y = int(pos[1])
for i in range(6):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    res += 1
print(res)
