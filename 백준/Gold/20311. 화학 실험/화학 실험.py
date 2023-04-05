import sys
input = sys.stdin.readline

N, K = map(int, input().split())
tmp = list(map(int, input().split()))
A = [0]*K
rlt = [0]*N

if N % 2: l = N // 2 + 1
else: l = N // 2

if max(tmp) > l:
    print(-1)
else:
    for k in range(K):
        A[k] = [tmp[k], k+1]        # [ 갯수, 색깔번호 ]

    A.sort()
    rlt[0] = A[-1][1]
    A[-1][0] -= 1
    if A[-1][0] == 0: A.pop()
    for i in range(1, N):
        if rlt[i-1] != A[-1][1]:
            rlt[i] = A[-1][1]
            A[-1][0] -= 1
            if A[-1][0] == 0:
                A.pop()
        else:
            rlt[i] = A[-2][1]
            A[-2][0] -= 1
            if A[-2][0] == 0:
                A.pop(-2)

    print(*rlt)