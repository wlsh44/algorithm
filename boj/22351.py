def cmp(N):
    for A in range(1, 1000):
        B = A
        ans = ''
        while len(ans) < len(N):
            ans += str(B)
            if ans == N:
                return A, B
            B += 1
    return None, None


N = input()
print(*cmp(N))

