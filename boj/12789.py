N = int(input())

arr = list(map(int, input().split()))
s = []

cur = 1
for num in arr:
    while s and s[-1] == cur:
        s.pop()
        cur += 1
    if num == cur:
        cur += 1
    else:
        s.append(num)
while s and s[-1] == cur:
    s.pop()
    cur += 1
print("Sad" if s else "Nice")