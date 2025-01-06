A, B = map(int, input().split())

K = A - B
x, y = A - 2 * (K - 1), B - (K - 1)
if A <= B or x <= 0 or y <= 0 or x - y != 1:
    print("NO")
else:
    print("YES")
    print(K)
    for _ in range(K - 1):
        print("aba")
    print("ab" * y + "a")
