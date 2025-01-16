T = int(input())

for _ in range(T):
    j, N = map(int, input().split())

    arr = []
    for _ in range(N):
        R, C = map(int, input().split())
        arr.append(R * C)

    arr.sort(reverse=True)

    ans = 0
    cnt = 0
    for size in arr:
        if cnt < j:
            cnt += size
            ans += 1
    print(ans)
