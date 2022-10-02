n = int(input())

s1 = [i for i in range(n, 0, -1)]
s1_set = set(s1)
s2 = []
ans = [int(input()) for _ in range(n)]
ans.reverse()
res = []

while s1 or s2:
    ans_num = ans.pop()

    # 스택에 없는 경우
    if ans_num in s1_set:
        num = s1.pop()
        s1_set.remove(num)
        while num != ans_num:
            s2.append(num)
            num = s1.pop()
            s1_set.remove(num)
            res += "+"
        s2.append(num)
        res += "+"
    elif s2[-1] != ans_num:
        print("NO")
        exit()
    s2.pop()
    res += "-"
print("\n".join(res))



# 1 2 3 4 5 6 7 8
#
#
# push 4
# 1 2 3 4
#
# pop 2
# 1 2
#
# push 2
# 1 2 5 6
#
# pop 1
#
# push 2
# 1 2 5 7 8
#
# pop 5

# push 1
# 1
# pop 1
# push 1
# 2
# pop 1
# push 3
# 3 4 5
# pop 1
# 3 4