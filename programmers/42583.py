from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length - 1)])
    sum_ = 0
    while sum_ != 0 or truck_weights:
        if sum_ != 0:
            sum_ -= bridge.pop()
        if truck_weights and sum_ + truck_weights[0] <= weight:
            bridge.appendleft(truck_weights.popleft())
            sum_ += bridge[0]
        else:
            bridge.appendleft(0)
        answer += 1
    return answer