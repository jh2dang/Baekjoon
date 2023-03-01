import sys
input = sys.stdin.readline

M, N = map(int, input().split())
K = int(input())

A = [[0]*M for _ in range(N)]
i = N-1
j = 0
k = 2
A[i][j] = 1
while k <= K:
    cnt = 0
    while i-1 >= 0 and A[i-1][j] == 0 and k<=K:
        A[i-1][j] = k
        i -= 1
        k += 1
        cnt += 1
    while j+1 < M and A[i][j+1] == 0 and k<=K:
        A[i][j+1] = k
        j += 1
        k += 1
        cnt += 1
    while i+1 < N and A[i+1][j] == 0 and k<=K:
        A[i+1][j] = k
        i += 1
        k += 1
        cnt += 1
    while j-1 >= 0 and A[i][j-1] == 0 and k<=K:
        A[i][j-1] = k
        j -= 1
        k += 1
        cnt += 1
    if cnt == 0: break
if k < K:
    print('0')
else:
    print(f'{j+1} {N-i}')
# for i in range(N):
#     print(A[i])