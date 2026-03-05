def solution(info, n, m):
    answer = 0

    dp = [[1000000] * m for i in range(len(info) + 1)]
    dp[0][0] = 0
    for i in range(1, len(info) + 1):
        a = info[i - 1][0]
        b = info[i - 1][1]
        for j in range(m):
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + a)

            if j + b < m:
                dp[i][j + b] = min(dp[i][j + b], dp[i - 1][j])

    answer = min(dp[-1])
    return answer if answer < n else -1
