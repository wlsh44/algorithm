from collections import deque


def to_minute(time):
    hour, minute = map(int, time.split(":"))
    return hour * 60 + minute


def solution(plans):
    answer = []

    for i in range(len(plans)):
        plans[i][1] = to_minute(plans[i][1])
        plans[i][2] = int(plans[i][2])

    new = deque(sorted(plans, key=lambda x: x[1]))
    stop = []

    time = new[0][1]
    cur = []
    while new or stop:
        if new and time == new[0][1]:
            if cur and cur[2] > 0:
                stop.append(cur)
            cur = new.popleft()
        cur[2] -= 1
        time += 1
        if cur[2] == 0:
            answer.append(cur[0])
            if stop:
                cur = stop.pop()
    answer.append(cur[0])
    return answer