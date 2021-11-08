def solution(clothes):
    dic = dict()
    for c in clothes:
        if c[1] not in dic:
            dic[c[1]] = 2
        else:
            dic[c[1]] += 1
    answer = 1
    for _, value in dic.items():
        answer *= value
    return answer - 1