X = input()

ans = 0
Y = 0
for num in X:
    Y += int(num)
if int(X) < Y and int(X) % 3 == 0:
    print(0)
    print("YES")
    exit()
while int(X) >= 10:
    Y = 0
    for num in X:
        Y += int(num)
    X = str(Y)
    ans += 1
print(ans)
print("YES" if Y % 3 == 0 else "NO")
