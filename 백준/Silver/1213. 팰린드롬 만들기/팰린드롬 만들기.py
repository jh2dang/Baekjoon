A = list(input())
f = []
l = []
m = []

while A:
    if A.count(A[0]) >= 2:
        t = A[0]
        f.append(A.pop(0))
        for i in range(len(A)):
            if A[i] == t:
                l.append(t)
                A.remove(t)
                break
    elif A.count(A[0]) == 1:
        m.append(A.pop(0))
if len(m) > 1: print("I'm Sorry Hansoo")
elif len(f)==len(l):
    f = list(sorted(f))
    rlt = f + m + list(reversed(f))
    print(*rlt, sep='')