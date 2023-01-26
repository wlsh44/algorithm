A = list(input())
B = list(input())

dp = [0] * len(A)
for i in range(len(B)):
    num = 0
    for j in range(len(A)):
        if num < dp[j]:
            num = dp[j]
        elif B[i] == A[j]:
            dp[j] = num + 1
if dp:
    print(max(dp))
else:
    print(0)