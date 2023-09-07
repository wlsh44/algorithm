N = int(input())

for i in range(N - 1):
    print((N - i - 2) * " ", end=" ")
    print((i * 2 + 1) * "*")
print("*" * (N * 2 - 1))
for i in range(N - 1):
    print(i * " ", end=" ")
    print(((N - i - 2) * 2 + 1) * "*")
