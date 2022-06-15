N, M = map(int, input().split())

string_set = set(input() for _ in range(N))
res = 0
for _ in range(M):
    string = input()
    if string in string_set:
        res += 1
print(res)

