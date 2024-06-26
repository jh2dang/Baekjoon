def solution(n):
    A = [[0] * n for _ in range(n)]
    x, y = -1, 0
    num = 1
    answer = []
    
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1          
            elif i % 3 == 1:
                y += 1            
            elif i % 3 == 2:
                x -= 1
                y -= 1      
            A[x][y] = num
            num += 1
            
    for i in A:
        for j in i:
            if j:
                answer.append(j)
    return answer