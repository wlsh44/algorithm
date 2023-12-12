import sys, heapq

input = sys.stdin.readline
n = int(input())

graph = [list(map(int, list(input().strip()))) for _ in range(n)]
d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
dist = [[int(1e9)] * n for _ in range(n)]

def dijkstra(y, x):
    dist[y][x] = 0
    q = []
    heapq.heappush(q, (0, (y, x)))

    while q:
        cur_cost, cur_pos = heapq.heappop(q)
        cur_y, cur_x = cur_pos

        if dist[cur_y][cur_x] < cur_cost:
            continue
        for dy, dx in d:
            ny, nx = cur_y + dy, cur_x + dx
            if 0 <= ny < n and 0 <= nx < n:
                cost = 1 if graph[ny][nx] == 0 else 0
                new_cost = cost + cur_cost
                if new_cost < dist[ny][nx]:
                    dist[ny][nx] = new_cost
                    heapq.heappush(q, (new_cost, (ny, nx)))


dijkstra(0, 0)
print(dist[n - 1][n - 1] if dist[n - 1][n - 1] != int(1e9) else 0)
