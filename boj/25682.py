import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

arr = [list(input().strip()) for _ in range(N)]
acu_w = [[0] * (M + 1) for _ in range(N + 1)]
acu_b = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(N):
    for j in range(M):
        acu_w[i + 1][j + 1] = acu_w[i][j + 1] + acu_w[i + 1][j] - acu_w[i][j]
        acu_b[i + 1][j + 1] = acu_b[i][j + 1] + acu_b[i + 1][j] - acu_b[i][j]
        if ((i + j) % 2 == 0 and arr[i][j] == "B") or ((i + j) % 2 == 1 and arr[i][j] == "W"):
            acu_w[i + 1][j + 1] += 1
        if ((i + j) % 2 == 0 and arr[i][j] == "W") or ((i + j) % 2 == 1 and arr[i][j] == "B"):
            acu_b[i + 1][j + 1] += 1

res = sys.maxsize

for i in range(1, N - K + 2):
    for j in range(1, M - K + 2):
        white_res = acu_w[i + K - 1][j + K - 1] - acu_w[i + K - 1][j - 1] - acu_w[i - 1][j + K - 1] + acu_w[i - 1][j - 1]
        black_res = acu_b[i + K - 1][j + K - 1] - acu_b[i + K - 1][j - 1] - acu_b[i - 1][j + K - 1] + acu_b[i - 1][j - 1]
        res = min(res, white_res, black_res)

print(res)