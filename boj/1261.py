import sys, heapq


input = sys.stdin.readline
M, N = map(int, input().split())

graph = [list(map(int, list(input().strip()))) for _ in range(N)]
dist = [[int(1e9)] * M for _ in range(N)]

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dijkstra(y, x):
    q = []
    dist[y][x] = 0
    heapq.heappush(q, (0, (y, x)))

    while q:
        cur_cost, cur = heapq.heappop(q)
        cur_y, cur_x = cur

        if dist[cur_y][cur_x] < cur_cost:
            continue
        for dy, dx in d:
            ny, nx = cur_y + dy, cur_x + dx

            if 0 <= ny < N and 0 <= nx < M:
                new_cost = cur_cost + graph[ny][nx]
                if new_cost < dist[ny][nx]:
                    dist[ny][nx] = new_cost
                    heapq.heappush(q, (new_cost, (ny, nx)))


dijkstra(0, 0)
print(dist[N - 1][M - 1])
