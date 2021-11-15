import heapq as hq
def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)
    while scoville[0] < K and len(scoville) >= 2:
        first = hq.heappop(scoville)
        second = hq.heappop(scoville)
        if first == 0 and second == 0:
            return -1
        hq.heappush(scoville, first + second * 2)
        answer += 1
    if scoville[0] < K:
        return -1
    return answer