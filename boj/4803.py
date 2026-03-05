import sys


input = sys.stdin.readline


def dfs(node):
    visit.add(node)
    s = [(node, 0)]

    while s:
        cur, parent = s.pop()

        for nxt in tree[cur]:
            if nxt == parent:
                continue
            if nxt in visit:
                return False
            visit.add(nxt)
            s.append((nxt, cur))
    return True


case = 0
while True:
    case += 1
    visit = set()
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    tree = {i: [] for i in range(1, n + 1)}

    for _ in range(m):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    ans = 0
    for node in range(1, n + 1):
        if node not in visit and dfs(node):
            ans += 1
    if ans == 0:
        print(f"Case {case}: No trees.")
    elif ans == 1:
        print(f"Case {case}: There is one tree.")
    else:
        print(f"Case {case}: A forest of {ans} trees.")