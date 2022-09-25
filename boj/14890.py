N, L = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

res = 0
def check_line(line):
    check = [True] * len(line)
    for i in range(N - 1):
        if line[i] == line[i + 1]:
            continue
        elif line[i] - line[i + 1] == 1:
            tmp = line[i + 1]
            if i + L >= N:
                return 0
            for j in range(L):
                if line[i + 1 + j] != tmp or check[i + 1 + j] == False:
                    return 0
                check[i + 1 + j] = False
        elif line[i] - line[i + 1] == -1:
            tmp = line[i]
            if i - L + 1 < 0:
                return 0
            for j in range(L):
                if line[i - j] != tmp or check[i - j] == False:
                    return 0
                check[i - j] = False
        else:
            return 0
    return 1

for i in range(N):
    res += check_line(arr[i])
    res += check_line([arr[j][i] for j in range(N)])
print(res)