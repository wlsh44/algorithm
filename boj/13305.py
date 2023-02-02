import sys

input = sys.stdin.readline
N = int(input())

street = [*map(int, input().split())]
gas = [*map(int, input().split())]

res = 0
min_gas = sys.maxsize
for i in range(len(street)):
    if gas[i] < min_gas:
        min_gas = gas[i]
    res += street[i] * min_gas
print(res)