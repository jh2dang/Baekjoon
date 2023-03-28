import sys
input = sys.stdin.readline

def nomat(si, sj, Hp, cnt):
    global mincho, MAX

    for ni, nj in mincho:
        d = abs(si - ni) + abs(sj - nj)
        if A[ni][nj] == 2 and d <= Hp:
            A[ni][nj] = 0
            nomat(ni, nj, Hp-d+H, cnt+1)
            A[ni][nj] = 2

    else:
        if abs(homei - si) + abs(homej - sj) <= Hp:
            if MAX < cnt:
                MAX = cnt

N, M, H = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
mincho = []
MAX = 0
for i in range(N):
    for j in range(N):
        if A[i][j] == 1:
            homei, homej = i, j
        elif A[i][j] == 2:
            mincho.append((i, j))
nomat(homei, homej, M, 0)
print(MAX)

