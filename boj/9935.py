import sys

input = sys.stdin.readline

s = input().rstrip()
boom_s = input().rstrip()
ans = []
for c in s:
    ans.append(c)
    if c == boom_s[-1] and "".join(ans[-len(boom_s):]) == boom_s:
        for _ in range(len(boom_s)):
            ans.pop()
if len(ans) == 0:
    print("FRULA")
else:
    print("".join(ans))