import sys, math

input = sys.stdin.readline

MAX = 4001
cnt = [0] * MAX
arr = []

N = int(input())

for _ in range(N):
    num = int(input())
    cnt[num] += 1
    arr.append(num)

if (sum(arr) // len(arr)) - (sum(arr) % len(arr)) >= 0.5:
    print(math.ceil(sum(arr) / len(arr)))
else:
    print(math.floor(sum(arr) / len(arr)))
arr.sort()
cnt.sort()
print(arr[len(arr) // 2])
if cnt[len(cnt) - 1] == cnt[len(cnt) - 2]:
    print()
print(arr[len(arr) - 1] - arr[0])

