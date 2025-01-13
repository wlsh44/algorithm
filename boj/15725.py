s = input()
p = s.split('x')

if s[0] == 'x':
    print(1)
elif s[0] == '-' and s[1] == 'x':
    print(-1)
elif len(p) >= 2:
    print(p[0])
else:
    print(0)

