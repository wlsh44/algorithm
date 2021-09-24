import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    stocks = list(map(int, input().split()))
    max_ = stocks[-1]
    profit = 0
    while stocks:
        stock = stocks.pop()
        if max_ < stock:
            max_ = stock
        else:
            profit += max_ - stock
    print(profit)

