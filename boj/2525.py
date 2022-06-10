m, s = map(int, input().split())
time = int(input())

s += time % 60
m += time // 60 + s // 60


print(f"{m % 24} {s % 60}")

