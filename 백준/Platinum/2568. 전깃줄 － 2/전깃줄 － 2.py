from bisect import bisect_left
import sys
input = sys.stdin.readline

N = int(input())

zul = []

for n in range(N):
    a, b = map(int, input().split())
    zul.append([a, b])

zul.sort()

# zul = [[1, 8], [2, 2], [3, 9], [4, 1], [6, 4], [7, 6], [9, 7], [10, 10]]


A = [0]*N

for n in range(N):
    A[n] = zul[n][1]

# A = [8, 2, 9, 1, 4, 6, 7, 10]

# ====================여기부터 LIS 만들기 시작
L = []
dp = [0]*N      # 인덱스 저장하는 리스트

for i in range(N):
    if not L or L[-1] < A[i]:
        L.append(A[i])
        dp[i] = len(L)-1
    else:
        idx = bisect_left(L, A[i])
        L[idx] = A[i]
        dp[i] = idx

# L = [1, 4, 6, 7, 10]
# dp = [0, 0, 1, 0, 1, 2, 3, 4]


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


# rlt = [1, 4, 6, 7, 10]
# DEL = [1, 2, 3] (dp에서 rlt뺀것)


print(len(DEL))
for ans in DEL:
    print(ans)