import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    F = list(sys.stdin.readline().strip())
    N = int(sys.stdin.readline().strip())
    A = sys.stdin.readline().strip()[1:-1].split(",")
    if A == ['']:
        A = []
    # print(A)
    cntr = 0
    dkv = 0
    enl = 0
    t = len(A)
    for i in range(len(F)):
        if F[i] == "R":
            cntr += 1
        else:
            if cntr % 2 == 0:
                dkv += 1
            else:
                enl += 1
    # print('앞:', dkv)
    # print('뒤:', enl)
    # print('R몇개:', cntr)
    # print(len(A))
    if dkv + enl > len(A):
        print('error')
    else:
        if cntr % 2 == 0:
            if enl == 0:
                A = A[dkv:]
            else:
                A = A[dkv:-enl]
        else:
            A = list(reversed(A))
            if dkv == 0:
                A = A[enl:]
            else:
                A = A[enl:-dkv]
        rlt = ''
        for i in range(len(A)):
            rlt += A[i]
        rlt = '[' + ','.join(A) + ']'
        print(rlt)