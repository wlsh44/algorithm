# 주차장 1~N
# 매일 아침 비어있는 상태에서 시작
# 차 옴 -> 주차 공간 확인 -> 공간 없으면 입구 대기
# 공간 하나, 차 하나 바로 떠남 -> 해당 장소 주차
# 주차 공간 여러 대 -> 번호가 가장 작은 공간 주차
# 주차료 = 차량의 무게 * 주차 공간 단위 무게당 요금
# 주차장 총 수입?
from collections import deque

N, M = map(int, input().split())

rs = [int(input()) for _ in range(N)]
wk = [int(input()) for _ in range(M)]
park = [0 for _ in range(N)]
q = deque([])

ans = 0
for _ in range(M * 2):
    car = int(input())
    if car > 0:
        flag = False
        for i in range(N):
            if park[i] == 0:
                park[i] = car
                flag = True
                break
        if not flag:
            q.append(car)
    else:
        car = car * -1
        for i in range(N):
            if park[i] == car:
                park[i] = 0
                ans += rs[i] * wk[car - 1]
                if q:
                    out = q.popleft()
                    park[i] = out
                break
print(ans)
