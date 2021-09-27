import sys

input = sys.stdin.readline

N = int(input())
dic = {}
for _ in range(N):
    item = input().strip()
    if item in dic:
        dic[item] += 1
    else:
        dic[item] = 1
dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
print(dic[0][0])