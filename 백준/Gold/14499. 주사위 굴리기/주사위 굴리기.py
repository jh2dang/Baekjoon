N, M, X, Y, P = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
rnffu = list(map(int, input().split()))
A = [0, 0, 0, 0]
B = [0, 0, 0]

for r in range(P):
    if rnffu[r] == 1 and Y + 1 < M:
        Y = Y + 1
        tmp = [B[0], B[1], B[2], A[3]]
        B[0] = tmp[3]
        B[1] = tmp[0]
        B[2] = tmp[1]
        A[3] = tmp[2]
        A[1] = B[1]
        print(B[1])
        if Map[X][Y] == 0:
            Map[X][Y] = A[3]
        else:
            A[3] = Map[X][Y]
            Map[X][Y] = 0
    if rnffu[r] == 2 and Y - 1 >= 0:
        Y = Y - 1
        tmp = [B[0], B[1], B[2], A[3]]
        B[0] = tmp[1]
        B[1] = tmp[2]
        B[2] = tmp[3]
        A[3] = tmp[0]
        A[1] = B[1]
        print(B[1])
        if Map[X][Y] == 0:
            Map[X][Y] = A[3]
        else:
            A[3] = Map[X][Y]
            Map[X][Y] = 0
    if rnffu[r] == 3 and X - 1 >= 0:
        X = X - 1
        tmp = [A[0], A[1], A[2], A[3]]
        A[0] = tmp[1]
        A[1] = tmp[2]
        A[2] = tmp[3]
        A[3] = tmp[0]
        B[1] = A[1]
        print(B[1])
        if Map[X][Y] == 0:
            Map[X][Y] = A[3]
        else:
            A[3] = Map[X][Y]
            Map[X][Y] = 0
    if rnffu[r] == 4 and X + 1 < N:
        X = X + 1
        tmp = [A[0], A[1], A[2], A[3]]
        A[0] = tmp[3]
        A[1] = tmp[0]
        A[2] = tmp[1]
        A[3] = tmp[2]
        B[1] = A[1]
        print(B[1])
        if Map[X][Y] == 0:
            Map[X][Y] = A[3]
        else:
            A[3] = Map[X][Y]
            Map[X][Y] = 0
    # print(A)
    # print(B)
    # print(Map)
    # print('-----------------------')