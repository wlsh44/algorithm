S = int(input())

N = 1
num = 2
while num < S:
    num += N + 2
    N += 1
print(N)