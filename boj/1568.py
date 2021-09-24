N = int(input())
K = 1
time = 0
while N > 0:
    if K > N:
        K = 1
    N -= K
    time += 1
    K += 1
print(time)