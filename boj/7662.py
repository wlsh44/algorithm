import sys, heapq

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    container = {}
    min_pq = []
    max_pq = []
    for key in range(k):
        cmd, num = input().split()
        num = int(num)
        if cmd == "I":
            container[key] = True
            heapq.heappush(min_pq, (num, key))
            heapq.heappush(max_pq, (-num, key))
        elif cmd == "D":
            if num == 1:
                while max_pq and container[max_pq[0][1]] is False:
                    heapq.heappop(max_pq)
                if not max_pq:
                    continue
                _, idx = heapq.heappop(max_pq)
                container[idx] = False
            elif num == -1 and min_pq:
                while min_pq and container[min_pq[0][1]] is False:
                    heapq.heappop(min_pq)
                if not min_pq:
                    continue
                _, idx = heapq.heappop(min_pq)
                container[idx] = False

    while max_pq and container[max_pq[0][1]] is False:
        heapq.heappop(max_pq)
    while min_pq and container[min_pq[0][1]] is False:
        heapq.heappop(min_pq)
    if max_pq:
        print(-max_pq[0][0], min_pq[0][0])
    else:
        print("EMPTY")