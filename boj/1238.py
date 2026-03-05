import sys, heapq

input = sys.stdin.readline
N, M, X = map(int, input().split())

graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start, dist):
    q = []
    dist[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        cur_cost, cur_node = heapq.heappop(q)

        if dist[cur_node] < cur_cost:
            continue
        for node, cost in graph[cur_node]:
            new_cost = cur_cost + cost
            if new_cost < dist[node]:
                dist[node] = new_cost
                heapq.heappush(q, (new_cost, node))


ans = 0
for i in range(1, N + 1):
    dist1 = [int(1e9)] * (N + 1)
    dist2 = [int(1e9)] * (N + 1)
    dijkstra(i, dist1)
    dijkstra(X, dist2)
    ans = max(ans, dist1[X] + dist2[i])
print(ans)
