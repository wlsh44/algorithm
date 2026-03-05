import sys


input = sys.stdin.readline

K, L = map(int, input().split())

graph = {input().strip(): i for i in range(L)}

arr = [(v, k) for k, v in graph.items()]
arr.sort(key=lambda x: x[0])

i = 0
while i < len(arr) and i < K:
    print(arr[i][1])
    i += 1
