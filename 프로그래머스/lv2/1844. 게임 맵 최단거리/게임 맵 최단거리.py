from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    V = [[-1]*m for _ in range(n)]
    V[0][0] = 1
    queue = deque()
    queue.append((0, 0))
    
    def bfs():
        while queue:
            si, sj = queue.popleft()
            
            for k in range(4):
                ni = si + di[k]
                nj = sj + dj[k]
                if 0 <= ni < n and 0 <= nj < m and V[ni][nj] == -1 and maps[ni][nj] == 1:
                    V[ni][nj] = V[si][sj] + 1
                    queue.append((ni, nj))
                    
    bfs()
    answer = V[n-1][m-1]
    return answer
