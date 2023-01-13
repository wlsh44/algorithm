import sys
from collections import deque

input = sys.stdin.readline

dice = [1, 2, 3, 4, 5, 6]

board = [i for i in range(101)]
dist = [0] * 101
N, M = map(int, input().split())
for _ in range(N + M):
    x, y = map(int, input().split())
    board[x] = y


def bfs():
    q = deque([1])

    while q:
        x = q.popleft()
        if x != board[x]:
            dist[board[x]] = dist[x]
            x = board[x]
        if x == 100:
            return dist[x]
        for dx in dice:
            nx = x + dx
            if nx <= 100 and dist[nx] == 0:
                dist[nx] = dist[x] + 1
                q.append(nx)


print(bfs())