N = int(input())

res = 0


def method_name(div_num, i):
    num = 0
    while i % div_num == 0:
        i //= div_num
        num += 1
    return num


num2, num5 = 0, 0
for i in range(1, N + 1):
    num2 += method_name(2, i)
    num5 += method_name(5, i)

print(min(num2, num5))