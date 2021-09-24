N, B = map(int, input().split())
base = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = ''
if N == 0:
    print(0)
else:
    while True:
        N, mod = divmod(N, B)
        num += base[mod]
        if N < B:
            num += base[N]
            break
    print(num[::-1])
