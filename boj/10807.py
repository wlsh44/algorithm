N = int(input())
arr = list(map(int, input().split()))
v = int(input())
res = 0
for num in arr:
    if num == v:
        res += 1
print(res)