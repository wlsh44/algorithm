import sys, heapq
input = sys.stdin.readline
N, E = map(int, input().split())

graph = {i: [] for i in range(1, N + 1)}
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
u, v = map(int, input().split())


def dijkstra(start):
    hq = []
    dist = [sys.maxsize] * (N + 1)
    heapq.heappush(hq, (0, start))
    dist[start] = 0
    while hq:
        cost, node = heapq.heappop(hq)

        if dist[node] < cost:
            continue
        for adj, adj_cost in graph[node]:
            new_cost = dist[node] + adj_cost

            if new_cost < dist[adj]:
                dist[adj] = new_cost
                heapq.heappush(hq, (new_cost, adj))

    return dist


start1 = dijkstra(1)
startU = dijkstra(u)
startV = dijkstra(v)
res = min(start1[u] + startU[v] + startV[N], start1[v] + startV[u] + startU[N])
if res >= sys.maxsize:
    print(-1)
else:
    print(res)