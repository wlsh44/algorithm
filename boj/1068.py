N = int(input())

arr = list(map(int, input().split()))
delete = int(input())

tree = {i: set() for i in range(N)}
root = 0
for i in range(N):
    if arr[i] == -1:
        root = i
        continue
    tree[arr[i]].add(i)

tree[delete] = []
s = [root]
res = 0
while s:
    n = s.pop()

    if n == delete:
        continue
    if delete in tree[n]:
        tree[n].remove(delete)
    if len(tree[n]) == 0:
        res += 1
    else:
        for x in tree[n]:
            s.append(x)
print(res)

# 0
# 1 2
#   4
#   5 6
#   3 7 8