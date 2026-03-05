import bisect


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))

    ans = 0
    for a in A:
        ans += bisect.bisect_left(B, a)
    print(ans)

