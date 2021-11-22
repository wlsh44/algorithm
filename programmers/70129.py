def solution(s):
    answer = [0, 0]
    while s != '1':
        tmp = ""
        for c in s:
            if c == '1':
                tmp += c
            else:
                answer[1] += 1
        length = format(len(tmp), 'b')
        s = length
        answer[0] += 1
    return answer