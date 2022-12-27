N = int(input())
F = int(input())

for i in range(100):
    if ((N - N % 100) + i) % F == 0:
        print(f"{i:02d}")
        break