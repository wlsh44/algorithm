from itertools import combinations


def solution(orders, course):
    answer = []

    d = {}
    for order in orders:
        for num in course:
            if num > len(order):
                break
            for comb in combinations(sorted(list(order)), num):
                key = "".join(comb)
                if key in d:
                    d[key] += 1
                else:
                    d[key] = 1
    new_c = {c: [] for c in course}
    for k, v in d.items():
        if v == 1:
            continue
        new_c[len(k)].append((k, v))
    for c in course:
        if not new_c[c]:
            continue
        new_c[c].sort(key=lambda x: -x[1])
        max_num = new_c[c][0][1]
        for k, v in new_c[c]:
            if v != max_num:
                break
            answer.append(k)
    answer.sort()
    return answer