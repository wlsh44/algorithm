T = int(input())

arr = [int(input()) for _ in range(T)]

quarter = 25
dime = 10
nickel = 5
penny = 1

for num in arr:
    remain1, num = divmod(num, quarter)
    remain2, num = divmod(num, dime)
    remain3, num = divmod(num, nickel)
    remain4, num = divmod(num, penny)
    print(remain1, remain2, remain3, remain4, end=" ")
    print()