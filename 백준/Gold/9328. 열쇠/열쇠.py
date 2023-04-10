from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    global V, munseo, cnt
    queue = deque()
    queue.append((0, 0))
    V[0][0] = 1

    while queue:
        nowi, nowj = queue.popleft()
        for k in range(4):
            ni = nowi + di[k]
            nj = nowj + dj[k]
            if 0 <= ni < h+2 and 0 <= nj < w+2 and A[ni][nj] != '*' and V[ni][nj] == 0:
                if A[ni][nj].isupper():
                    if A[ni][nj] in key:
                        V[ni][nj] = 1
                        queue.append((ni, nj))
                elif A[ni][nj].islower():
                    if A[ni][nj].upper() not in key:
                        key.append(A[ni][nj].upper())
                        V = [[0]*(w+2) for _ in range(h+2)]
                    V[ni][nj] = 1
                    queue.append((ni, nj))
                elif A[ni][nj] == '$':
                    if (ni, nj) not in munseo:
                        cnt += 1
                        munseo.append((ni, nj))
                    V[ni][nj] = 1
                    queue.append((ni, nj))
                else:
                    V[ni][nj] = 1
                    queue.append((ni, nj))


T = int(input())

for tc in range(1, T+1):
    h, w = map(int, input().split())
    A = [['.'] + list(input().strip()) + ['.'] for _ in range(h)]
    A.insert(0, ['.']*(w+2))
    A.append(['.']*(w+2))
    V = [[0]*(w+2) for _ in range(h+2)]

    munseo = []

    cnt = 0

    key = [i.upper() for i in list(input().strip())]

    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    bfs()

    print(cnt)