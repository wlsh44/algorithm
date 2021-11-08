A, P = map(int, input().split())
s = []
q = [A]
visited = {}

while True:
    v = q[-1]
    if v in visited:
        break
    visited[v] = True
    num = 0
    for c in str(v):
        num += int(c) ** P
    if num in visited:
        s = list(visited)
        i = s.index(num)
        s = s[:i]
        break
    q.append(num)
print(len(s))

