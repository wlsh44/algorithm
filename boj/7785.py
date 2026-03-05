N = int(input())

s = set()

for _ in range(N):
    name, log = input().split()

    if log == "enter":
        s.add(name)
    else:
        s.remove(name)
for name in sorted(s, reverse=True):
    print(name)
