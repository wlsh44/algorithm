import sys

sys.setrecursionlimit(10000)

def up(x, y, n, num, graph):
    if n == 0:
        return graph
    for _ in range(n):
        graph[x][y] = num
        num += 1
        x -= 1
        y -= 1
    return down(x + 2, y + 1, n - 1, num, graph)

def side(x, y, n, num, graph):
    if n == 0:
        return graph
    for i in range(y, y + n):
        graph[x][i] = num
        num += 1
    return up(x - 1, i - 1, n - 1, num, graph)

def down(x, y, n, num, graph):
    if n == 0:
        return graph
    for i in range(x, x + n):
        graph[i][y] = num
        num += 1
    return side(i, y + 1, n - 1, num, graph)

def solution(n):
    answer = []
    graph = [[0] * n for _ in range(n)]
    graph = down(0, 0, n, 1, graph)
    for idx, row in enumerate(graph):
        answer += row[:idx + 1]
    return answer