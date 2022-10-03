n = int(input())

s = []
ans = [int(input()) for _ in range(n)]
ans.reverse()
res = []
cur = 1
while ans:
    ans_num = ans.pop()

    while cur <= ans_num:
        s.append(cur)
        res += "+"
        cur += 1
    if s[-1] != ans_num:
        print("NO")
        exit()
    s.pop()
    res += "-"
print("\n".join(res))
