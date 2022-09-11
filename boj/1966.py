from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    arr = deque(list(map(int, input().split())))

    index = M
    res = 0
    while True:
        if arr[0] == max(arr):
            res += 1
            if index == 0:
                print(res)
                break
            arr.popleft()
        else:
            arr.rotate(-1)
        index = index - 1 if index != 0 else len(arr) - 1

