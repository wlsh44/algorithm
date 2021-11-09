def solution(priorities, location):
    answer = 0
    while True:
        idx = priorities.index(max(priorities))
        if location < idx:
            location += len(priorities[idx:])
        else:
            location -= len(priorities[:idx])
        priorities = priorities[idx:] + priorities[:idx]
        answer += 1
        if location == 0:
            break
        priorities.pop(0)
        location -= 1
    return answer