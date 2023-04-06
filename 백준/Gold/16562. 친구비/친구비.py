import sys
input = sys.stdin.readline


N, M, K = map(int, input().split())
don = list(map(int, input().split()))
V = [0]*(N+1)
num = 1
for _ in range(M):
    a, b = map(int, input().split())
    if not V[a] and not V[b]:
        V[a] = V[b] = num
        num += 1
    elif not V[a] or not V[b]:
        if V[a]: V[b] = V[a]
        else: V[a] = V[b]
    else:
        if V[a] != V[b]:
            MIN = min(V[a], V[b])
            MAX = max(V[a], V[b])
            for i in range(N+1):
                if V[i] == MAX:
                    V[i] = MIN

v = [0]*(num+1)
G = [1e9]*(num+1)
SUM = 0

for i in range(1, N+1):
    if V[i] == 0:
        SUM += don[i-1]
        if SUM > K:
            break
    else:
        if don[i-1] < G[V[i]]:
            G[V[i]] = don[i-1]
for g in range(len(G)):
    if G[g] != 1e9:
        SUM += G[g]
        if SUM > K:
            break
if SUM > K:
    print('Oh no')
else: print(SUM)