import sys

input = sys.stdin.readline
N = int(input())

arr = list(map(int, input().split()))
tmp = sorted(list(set(arr)))
dic = {tmp[i]: i for i in range(len(tmp))}
for pos in arr:
    print(dic[pos], end=" ")

