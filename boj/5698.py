while True:
    arr = list(input().split(" "))

    if arr[0][0] == "*":
        break
    c = arr[0][0].lower()
    flag = True
    for s in arr:
        if not s[0].lower().startswith(c):
            flag = False
            break
    print("Y" if flag else "N")
