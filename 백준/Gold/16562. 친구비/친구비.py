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
# print(V)
v = [0]*(num+1)
G = [[0] for _ in range(N+1)]
for i in range(1, N+1):
    if V[i] != 0:
        if not v[V[i]]:
            G[V[i]] = [1, don[i-1]]
            v[V[i]] = 1
        else:
            G[V[i]][0] += 1
            if don[i-1] < G[V[i]][1]:
                G[V[i]][1] = don[i-1]
# print(G)
# print(V)
SUM = 0
for g in range(len(G)):
    if len(G[g]) > 1:
        SUM += G[g][1]

for i in range(1, N+1):
    if not V[i]:
        SUM += don[i-1]
if SUM > K:
    print('Oh no')
else:
    print(SUM)