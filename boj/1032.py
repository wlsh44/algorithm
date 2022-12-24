N = int(input())

cmds = [list(input()) for _ in range(N)]

ans = cmds[0]

for cmd in cmds:
    for i in range(len(cmd)):
        if ans[i] != cmd[i]:
            ans[i] = "?"

print("".join(ans))