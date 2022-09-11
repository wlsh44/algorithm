from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    arr = deque(list(map(int, input().split())))
    priority = [0] * 10
    for num in arr:
        priority[num] += 1

    index = M
    res = 0
    flag = False
    for i in range(9, 0, -1):
        priority_cnt = priority[i]
        while priority_cnt != 0:
            if arr[0] == i:
                res += 1
                if index == 0:
                    flag = True
                    break
                priority_cnt -= 1
                arr.popleft()
            else:
                arr.rotate(-1)
            index = index - 1 if index != 0 else len(arr) - 1
        if flag:
            print(res)
            break