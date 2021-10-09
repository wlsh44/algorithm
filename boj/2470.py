import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
i, j = 0, len(arr) - 1
min_ = arr[j] + arr[i]
num1, num2 = arr[i], arr[j]
while i != j:
    if abs(arr[j] + arr[i]) < abs(min_):
        min_ = arr[j] + arr[i]
        num1 = arr[i]
        num2 = arr[j]
    if min_ == 0:
        break
    if arr[j] + arr[i] < 0:
        i += 1
    else:
        j -= 1

print(num1, num2)