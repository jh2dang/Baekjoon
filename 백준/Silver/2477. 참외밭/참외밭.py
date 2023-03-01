K = int(input())
A = [[]*5 for _ in range(5)]
D = []
L = []
for i in range(6):
    d, l = map(int, input().split())
    A[d].append(l)
    D.append(d)
    L.append(l)
D.extend([D[0], D[1], D[2]])
L.extend([L[0], L[1], L[2]])
for i in range(len(D)-3):
    if D[i:i+2] == D[i+2:i+4]:
        t = L[i+1]*L[i+2]
h = max(max(A[3]), max(A[4]))
w = max(max(A[1]), max(A[2]))
ans = (h*w-t)*K
print(ans)