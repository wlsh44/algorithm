A, B = map(int, input().split())

m = int(input())

arr = list(map(int, input().split()))

base_10 = 0
length = len(arr) - 1
for num in arr:
    base_10 += num * (A ** length)
    length -= 1

base_B = '' if base_10 != 0 else '0'
while base_10 > 0:
    base_10, mod = divmod(base_10, B)
    base_B = str(mod) + " " + base_B
print(base_B)
