arr = list(input())

zero = 0
one = 0
for i in range(len(arr) - 1):
    if arr[i] != arr[i + 1]:
        if arr[i] == '0':
            zero += 1
        else:
            one += 1
if arr[-1] == '0':
    zero += 1
else:
    one += 1
if zero <= one:
    print(zero)
else:
    print(one)
