N, K = map(int, input().split())

cnt = 0
while N != 1:
    if N % K == 0:
        N /= K
        cnt += 1
    else:
        tmp = (N % K)
        N -= tmp
        cnt += tmp
print(cnt)
