d = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

while True:
    R, C = map(int, input().split())
    if R == 0 and C == 0:
        break
    arr = [input() for _ in range(R)]
    ans = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j] == "*":
                ans[i][j] = -1
    for i in range(R):
        for j in range(C):
            if arr[i][j] == "*":
                for dy, dx in d:
                    if 0 <= i + dy < R and 0 <= j + dx < C and arr[i + dy][j + dx] != "*":
                        ans[i + dy][j + dx] += 1
    for i in range(R):
        for j in range(C):
            print(ans[i][j] if ans[i][j] != -1 else "*", end="")
        print("")
