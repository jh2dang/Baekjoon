def check(m, n, B):
    lst = []
    dx, dy = [0, 0, 1, 1], [0, 1, 1, 0]
    for i in range(m-1):
        for j in range(n-1):
            if B[i][j] != 0:
                ck_set = set()
                for k in range(4):
                    ck_set.add(B[i + dx[k]][j + dy[k]])
                if len(ck_set) == 1:
                    for k in range(4):
                        lst.append([i + dx[k], j + dy[k]])
    return lst

def del_down(m, n, B, lst):
    for i in lst:
            B[i[0]][i[1]] = 0
        
    for _ in range(m):
        for j in range(n):
            for i in range(m-1):
                if B[i][j] != 0 and B[i+1][j] == 0:
                    B[i][j], B[i+1][j] = 0, B[i][j]
    return B

def solution(m, n, board):
    B = [list(i) for i in board]
    
    while True:
        lst = check(m, n, B)
        if not lst:
            break
        B = del_down(m, n, B, lst)
        
    answer = 0
    for ans in B:
        answer += ans.count(0)
    
    return answer