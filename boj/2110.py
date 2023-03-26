import sys

input = sys.stdin.readline

N, C = map(int, input().split())

house = [int(input()) for _ in range(N)]
house.sort()
left, right = 1, house[-1] - house[0]
res = 0

while left <= right:
    mid = (left + right) // 2
    cnt = 1

    current_house = house[0]
    for i in range(1, N):
        if house[i] - current_house >= mid:
            cnt += 1
            current_house = house[i]
    if cnt >= C:
        res = mid
        left = mid + 1
    elif cnt < C:
        right = mid - 1

print(res)