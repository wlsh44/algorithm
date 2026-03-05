T = int(input())


def check_row():
    for i in range(9):
        check = set()
        for j in range(9):
            check.add(arr[i][j])
        if len(check) != 9:
            return False
    return True


def check_col():
    for i in range(9):
        check = set()
        for j in range(9):
            check.add(arr[j][i])
        if len(check) != 9:
            return False
    return True


def check_box():
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            check = set()
            for y in range(i, i + 3):
                for x in range(j, j + 3):
                    check.add(arr[y][x])
            if len(check) != 9:
                return False
    return True


for t in range(1, T + 1):
    if t != 1:
        input()
    arr = [list(map(int, input().split())) for _ in range(9)]

    flag = check_row() and check_col() and check_box()

    print(f"Case {t}: ", end="")
    print("CORRECT" if flag else "INCORRECT")
