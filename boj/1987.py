import sys


input = sys.stdin.readline

R, C = map(int, input().split())

graph = [list(input()) for _ in range(R)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
num = 0
visited = {graph[0][0]}

def dfs(y, x, visited, depth):
    global num

    num = max(num, depth)
    for dy, dx in d:
        ny, nx = y + dy, x + dx
        if 0 <= ny < R and 0 <= nx < C and graph[ny][nx] not in visited:
            visited.add(graph[ny][nx])
            dfs(ny, nx, visited, depth + 1)
            visited.remove(graph[ny][nx])


dfs(0, 0, visited, 1)
print(num)