import sys
import heapq

input = sys.stdin.readline

N = int(input())

arr = [int(input()) for _ in range(N)]
heapq.heapify(arr)

ans = 0
while len(arr) != 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    num = a + b
    ans += num
    heapq.heappush(arr, num)
print(ans)
