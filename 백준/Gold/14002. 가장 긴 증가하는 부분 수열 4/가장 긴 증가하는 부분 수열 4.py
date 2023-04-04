from bisect import bisect_left
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

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
for j in range(len(dp)-1, -1, -1):
    if dp[j] == MAX:
        rlt[MAX] = A[j]
        MAX -= 1
        if MAX == -1: break

print(len(L))
print(*rlt)