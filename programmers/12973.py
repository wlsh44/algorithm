from collections import deque

def solution(s):
    answer = -1
    s = deque(s)
    while True:
        if not s:
            answer = 1
            break
        tmp = deque([])
        length = len(s)
        while s:
            if tmp and tmp[-1] == s[0]:
                tmp.pop()
                s.popleft()
            else:
                tmp.append(s.popleft())
        if len(tmp) == length:
            answer = 0
            break
        s = tmp
    return answer