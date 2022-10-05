N = int(input())



def is_filled(arr, num):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != num:
                return False
    return True


def rec(arr, n):
    if is_filled(arr, 1):
        return 1, 0
    elif is_filled(arr, 0):
        return 0, 1

    white = 0
    blue = 0
    n //= 2
    b, w = rec([row[:n] for row in arr[:n]], n)
    white += w
    blue += b
    b, w = rec([row[n:] for row in arr[:n]], n)
    white += w
    blue += b
    b, w = rec([row[:n] for row in arr[n:]], n)
    white += w
    blue += b
    b, w = rec([row[n:] for row in arr[n:]], n)
    white += w
    blue += b
    return blue, white


arr = [list(map(int, input().split())) for _ in range(N)]
blue, white = rec(arr, N)
print(white)
print(blue)