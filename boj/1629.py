A, B, C = map(int, input().split())

num = A

def rec(power):
    if power == 1:
        return A % C

    divided_power = power // 2
    tmp = pow(rec(divided_power), 2) % C
    if power % 2 == 0:
        return tmp
    else:
        return (tmp * rec(1)) % C

print(rec(B))