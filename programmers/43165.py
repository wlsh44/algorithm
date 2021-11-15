def dfs(sum_, numbers, target, depth):
    if depth == len(numbers):
        if sum_ == target:
            return 1
        else:
            return 0
    return dfs(sum_ + numbers[depth], numbers, target, depth + 1) + dfs(sum_ - numbers[depth], numbers, target, depth + 1)


def solution(numbers, target):
    answer = dfs(0, numbers, target, 0)
    return answer