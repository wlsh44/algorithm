import heapq, sys


input = sys.stdin.readline
N, M = map(int, input().split())

graph = {i: [] for i in range(N + 1)}

for _ in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))



def dijkstra(node, dist):
    q = []
    heapq.heappush(q, (0, node))
    dist[node] = 0

    while q:
        cur_dist, cur_node = heapq.heappop(q)

        if dist[cur_node] < cur_dist:
            continue
        for n, d in graph[cur_node]:
            new_dist = dist[cur_node] + d
            if new_dist < dist[n]:
                dist[n] = new_dist
                heapq.heappush(q, (new_dist, n))


for _ in range(M):
    a, b = map(int, input().split())
    dist = [1e9] * (N + 1)
    dijkstra(a, dist)
    print(dist[b])