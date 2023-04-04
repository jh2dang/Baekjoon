from bisect import bisect_left
import sys
input = sys.stdin.readline

N = int(input())
zul = []

for n in range(N):
    a, b = map(int, input().split())
    zul.append([a, b])

zul.sort()

A = [0]*N

for n in range(N):
    A[n] = zul[n][1]

L = []
dp = [0]*N

for i in range(N):
    if not L or L[-1] < A[i]:
        L.append(A[i])
        dp[i] = len(L)-1
    else:
        idx = bisect_left(L, A[i])
        L[idx] = A[i]
        dp[i] = idx

MAX = max(dp)
rlt = [0]*(MAX+1)
DEL = [0]*(len(dp)-len(L))
cnt = 0
for j in range(len(dp)-1, -1, -1):
    if dp[j] == MAX:
        rlt[MAX] = A[j]
        MAX -= 1
    else:
        DEL[cnt] = zul[j][0]
        cnt += 1
DEL.sort()


print(len(DEL))
for ans in DEL:
    print(ans)