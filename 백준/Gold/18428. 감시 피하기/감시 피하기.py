N = int(input())
A = [list(input().split()) for _ in range(N)]
V = [[0]*N for _ in range(N)]

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
cnt = 0

def dd(x, y):
    global A, cnt
    for k in range(4):
        ti, tj = x, y
        for m in range(N):
            ni = x + m * di[k]
            nj = y + m * dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if A[ni][nj] == 'X':
                    ti, tj = ni, nj
                elif A[ni][nj] == 'O':
                    break
                elif A[ni][nj] == 'S':
                    if ti == x and tj == y:
                        cnt = 100
                    else:
                        A[ti][tj] = 'O'

def check(x, y):
    global A, cnt
    for k in range(4):
        for m in range(N):
            ni = x + m * di[k]
            nj = y + m * dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if A[ni][nj] == 'O':
                    V[ni][nj] += 1
                    break

def ss():
    global A, V, cnt
    for i in range(N):
        for j in range(N):
            if A[i][j] == 'T':
                dd(i, j)
    for i in range(N):
        for j in range(N):
            if A[i][j] == 'T':
                check(i, j)
    for i in range(N):
        for j in range(N):
            if V[i][j] != 0:
                cnt += 1
    if cnt <= 3:
        print('YES')
    else:
        print('NO')

ss()
# print(cnt)
# for i in range(N):
#     print(A[i])