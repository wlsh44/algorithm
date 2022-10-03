M = 1234567891
r = 31
L = int(input())
arr = list(input())

sum_ = 0
for i, c in enumerate(arr):
    num = ord(c) - ord('a') + 1
    sum_ += (num * (r ** i)) % M
print(sum_ % M)