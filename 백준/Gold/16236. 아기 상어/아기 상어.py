from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

A = [list(map(int, input().split())) for _ in range(N)]
di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]
sang = 2
cnt = 0
ans = 0

for i in range(N):
    for j in range(N):
        if A[i][j] == 9:
            si, sj = i, j

def bfs(si, sj):
    global d, sang, cnt
    V = [[-1] * N for _ in range(N)]
    mgg = []
    queue = deque()
    queue.append((si, sj))
    V[si][sj] = 0

    while queue:
        nowi, nowj = queue.popleft()

        for k in range(4):
            ni = nowi + di[k]
            nj = nowj + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if A[ni][nj] <= sang and V[ni][nj] == -1:
                    queue.append((ni, nj))
                    V[ni][nj] = V[nowi][nowj] + 1
                    if A[ni][nj] < sang and A[ni][nj] != 0:
                        mgg.append((V[ni][nj], ni, nj))

    return sorted(mgg)


while True:
    MGG = bfs(si, sj)
    A[si][sj] = 0

    if not MGG:
        break

    d, ni, nj= MGG.pop(0)
    A[ni][nj] = 0
    si = ni
    sj = nj
    cnt += 1
    if cnt == sang:
        cnt = 0
        sang += 1
    ans += d

print(ans)