x = int(input())
y = int(input())
res = 1

if x > 0 and y > 0:
    res = 1
elif x < 0 and y > 0:
    res = 2
elif x < 0 and y < 0:
    res = 3
else:
    res = 4
print(res)
