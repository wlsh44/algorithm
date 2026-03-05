N = int(input())

cur_set = {0}
for _ in range(N):
    tmp = set()
    for num in cur_set:
        tmp.add(num + 1)
        tmp.add(num + 5)
        tmp.add(num + 10)
        tmp.add(num + 50)
    cur_set = tmp
print(len(cur_set))
