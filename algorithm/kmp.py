def fail(b):
    f = [0]*(len(b))
    t = 0
    f[0] = 0
    #state numbers are adjusted to indices.
    for s in range(1, len(b)):
        while t > 0 and b[s] != b[t]:
            t = f[t-1]
        if b[s] == b[t]:
            t += 1
            f[s] = t
        else:
            f[s] = 0
    return f

def identify(a, b, f):
    s = 0
    for i in range(1, len(a)):
        #Complete this part according to the algorithm.
        while s > 0 and a[i] != b[s]:
            s = f[s - 1]
        if a[i] == b[s]:
            s += 1
        if s == len(b):
            return True
    return False

a = 'bababaabbab'
a1 = 'babababbaabb'
keyword = 'ababaa' #keyword
f = fail(keyword) #failure function

print(f) #[0, 0, 1, 2, 3, 1]
print(identify(a, keyword, f)) #True
print(identify(a1, keyword, f)) #False