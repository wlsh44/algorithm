import sys, heapq


input = sys.stdin.readline
n, m, r = map(int, input().split())

graph = {i: [0, []] for i in range(1, n + 1)}

items = list(map(int, input().split()))
for i in range(n):
    graph[i + 1][0] = items[i]

for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a][1].append((b, c))
    graph[b][1].append((a, c))


def dijkstra(start):
    q = []
    dist[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        cur_cost, cur_node = heapq.heappop(q)

        if dist[cur_node] < cur_cost:
            continue
        for node, cost in graph[cur_node][1]:
            new_cost = cost + cur_cost
            if new_cost < dist[node]:
                dist[node] = new_cost
                heapq.heappush(q, (new_cost, node))


ans = 0
for i in range(1, n + 1):
    dist = [int(1e9) for _ in range(n + 1)]
    dijkstra(i)
    tmp = 0
    for i, v in enumerate(dist):
        if i == 0:
            continue
        if v <= m:
            tmp += graph[i][0]
    ans = max(ans, tmp)

print(ans)

