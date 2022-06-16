import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
cards = list(map(int, input().split()))
counter = Counter(arr)

for card in cards:
    print(counter[card], end=" ")
