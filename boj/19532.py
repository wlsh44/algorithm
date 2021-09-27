a, b, c, d, e, f = map(int, input().split())

flag = False
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if d * x + e * y == f and a * x + b * y == c:
            flag = True
            print(x, y)
            break
    if flag:
        break

