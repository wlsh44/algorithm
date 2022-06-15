import sys
from collections import Counter

input = sys.stdin.readline

MAX = 8002

N = int(input())
cnt = [0] * MAX
arr = []
for _ in range(N):
    num = int(input())
    cnt[num + 4000] += 1
    arr.append(num)

arr.sort()

print(round(sum(arr) / N))
print(arr[len(arr) // 2])

counter = Counter(arr).most_common(2)
if len(counter) >= 2 and counter[0][1] == counter[1][1]:
    mode = counter[1][0]
else:
    mode = counter[0][0]

print(mode)
print(max(arr) - min(arr))
