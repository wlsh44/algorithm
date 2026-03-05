N = int(input())

ans = 0

for _ in range(N):
    s = []
    word = list(input())
    for c in word:
        if s and s[-1] == c:
            s.pop()
        else:
            s.append(c)
    if not s:
       ans += 1
print(ans)
