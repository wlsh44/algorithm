T = int(input())

for _ in range(T):
    N = int(input())
    arr = []
    for _ in range(N):
        s, t = map(int, input().split())
        if s > t:
            s, t = t, s
        s = (s - 1) // 2
        t = (t - 1) // 2
        arr.append((s, t))
    arr.sort()
    time = 0
    while arr:
        end = -1
        tmp = []
        for s, t in arr:
            if s > end:
                end = t
            else:
                tmp.append((s, t))
        arr = tmp
        time += 10
    print(time)
