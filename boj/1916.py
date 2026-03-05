import sys, heapq

input = sys.stdin.readline
N = int(input())
M = int(input())

graph = {i:[] for i in range(1, N + 1)}
dist = [int(1e9)] * (N + 1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        cur_cost, cur_node = heapq.heappop(q)

        if dist[cur_node] < cur_cost:
            continue
        for node, cost in graph[cur_node]:
            new_cost = cost + cur_cost
            if new_cost < dist[node]:
                dist[node] = new_cost
                heapq.heappush(q, (new_cost, node))


s, e = map(int, input().split())
dijkstra(s)
print(dist[e])
