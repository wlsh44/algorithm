while True:
    line = list(input())
    res = 0

    if line[0] == '#':
        break
    for c in line:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'I' or c == 'E' or c == 'A' or c == 'O' or c == 'U':
            res += 1
    print(res)