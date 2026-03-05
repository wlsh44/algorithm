pwd = input()
N = int(input())

words = [input() for _ in range(N)]

for i in range(26):
    decode = ""
    for c in pwd:
        if ord(c) + i <= ord('z'):
            decode += chr(ord(c) + i)
        else:
            decode += chr(ord(c) + i - 26)
    for word in words:
        if word in decode:
            print(decode)
            exit(0)
