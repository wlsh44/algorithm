def fatigue_sum(minerals, pick):
    fatigue = 0
    for mineral in minerals:
        if pick == 0:
            fatigue += 1
        elif pick == 1:
            if mineral == "diamond":
                fatigue += 5
            else:
                fatigue += 1
        else:
            if mineral == "diamond":
                fatigue += 25
            elif mineral == "iron":
                fatigue += 5
            else:
                fatigue += 1
    return fatigue


def sort_key(minerals):
    fatigue = 0
    for mineral in minerals:
        if mineral == "diamond":
            fatigue += 25
        elif mineral == "iron":
            fatigue += 5
        else:
            fatigue += 1
    return -fatigue


def solution(picks, minerals):
    answer = 0
    arr = []
    for i in range(len(minerals)):
        if i % 5 == 0:
            arr.append([])
        arr[-1].append(minerals[i])

    pick_cnt = sum(picks)
    arr = arr[:pick_cnt]
    arr.sort(key=lambda x: (sort_key(x), len(x)))
    pick = 0
    for minerals in arr:
        while picks[pick] == 0:
            pick += 1
        answer += fatigue_sum(minerals, pick)
        picks[pick] -= 1
    return answer