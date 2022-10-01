def is_palindrome(num):
    for i in range(len(num) // 2):
        if num[i] != num[len(num) - 1 - i]:
            return False
    return True

while True:
    num = list(input())
    if num == ["0"]:
        break
    if is_palindrome(num):
        print("yes")
    else:
        print("no")


