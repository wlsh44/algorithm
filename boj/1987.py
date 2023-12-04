import sys


input = sys.stdin.readline

R, C = map(int, input().split())

graph = [list(input()) for _ in range(R)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
num = 0
visited = {graph[0][0]}


def dfs(y, x, depth):
    global num

    num = max(num, depth)
    for i in range(4):
        ny, nx = y + d[i][0], x + d[i][1]
        if 0 <= ny < R and 0 <= nx < C and graph[ny][nx] not in visited:
            visited.add(graph[ny][nx])
            dfs(ny, nx, depth + 1)
            visited.remove(graph[ny][nx])


dfs(0, 0, 1)
print(num)

