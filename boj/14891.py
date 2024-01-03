import sys
from collections import deque

input = sys.stdin.readline
arr = [[]]
for _ in range(4):
    arr.append(deque(map(int, list(input().strip()))))

K = int(input())

for _ in range(K):
    index, rotate = map(int, input().split())

    rotate_dict = {index: rotate}
    r_rotate = rotate * -1
    for i in range(index, 4):
        if arr[i][2] != arr[i + 1][6]:
            rotate_dict[i + 1] = r_rotate
            r_rotate *= -1
        else:
            break
    l_rotate = rotate * -1
    for i in range(index, 1, -1):
        if arr[i - 1][2] != arr[i][6]:
            rotate_dict[i - 1] = l_rotate
            l_rotate *= -1
        else:
            break
    for key, val in rotate_dict.items():
        arr[key].rotate(val)

print(arr[1][0] + arr[2][0] * 2 + arr[3][0] * 4 + arr[4][0] * 8)
