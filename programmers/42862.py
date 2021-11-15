def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    reserve, lost = list(set(reserve) - set(lost)), list(set(lost) - set(reserve))
    for r in reserve:
        if r - 1 in lost:
            lost.remove(r - 1)
        elif r + 1 in lost:
            lost.remove(r + 1)
    answer = n - len(lost)
    return answer