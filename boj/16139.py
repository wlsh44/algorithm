import sys


input = sys.stdin.readline

s = input().rstrip()

N = int(input())

arr = [[0 for _ in range(len(s))] for _ in range(26)]

alpha = ord(s[0]) - ord('a')
arr[alpha][0] += 1
for i in range(1, len(s)):
    alpha = ord(s[i]) - ord('a')
    arr[alpha][i] += 1
    for j in range(26):
        arr[j][i] += arr[j][i - 1]

for _ in range(N):
    res = 0
    find, l, r = input().split()
    l, r = int(l), int(r)

    alpha = ord(find) - ord('a')
    if l > 0:
        print(arr[alpha][r] - arr[alpha][l - 1])
    else:
        print(arr[alpha][r])
