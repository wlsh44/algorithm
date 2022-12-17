N = int(input())
M = int(input())
S = list(input())

i = 0
ioi = []

res = 0
while i < len(S):
    char = "I"
    cnt = 0
    while i < len(S) and S[i] == char:
        i += 1
        char = "O" if char == "I" else "I"
        if i < len(S) and S[i] == "I" and char == "I":
            cnt += 1
            if cnt >= N:
                res += 1
    if i < len(S) and S[i] == "O":
        i += 1
print(res)