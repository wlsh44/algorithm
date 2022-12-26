import sys

input = sys.stdin.readline

N, M = map(int, input().split())

note = {}
for _ in range(N):
    site, pwd = input().split()
    note[site] = pwd

for _ in range(M):
    print(note[input().strip()])
