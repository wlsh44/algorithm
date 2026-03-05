import sys, heapq

INF = int(1e9)
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

graph = {i: [] for i in range(1, N + 1)}
dist = [INF] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append((B, 1))


def dijkstra(start):
    q = []
    dist[start] = 0
    heapq.heappush(q, (dist[start], start))

    while q:
        cur_cost, cur_node = heapq.heappop(q)

        if dist[cur_node] < cur_cost:
            continue
        for node, cost in graph[cur_node]:
            new_cost = cost + cur_cost
            if new_cost < dist[node]:
                dist[node] = new_cost
                heapq.heappush(q, (new_cost, node))


dijkstra(X)
ans = list(filter(lambda x: dist[x] == K, range(1, N + 1)))
ans.sort()
if len(ans) == 0:
    print(-1)
else:
    print(*ans, sep="\n")
