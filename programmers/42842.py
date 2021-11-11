def solution(brown, yellow):
    answer = []
    size = brown + yellow
    for weight in range(3, size):
        if size % weight != 0: continue
        height = size / weight
        if 2 * height + 2 * weight - 4 == brown:
            answer = [weight, height]
    return answer