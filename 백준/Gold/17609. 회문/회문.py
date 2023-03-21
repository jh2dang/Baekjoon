T = int(input())

for _ in range(1, T+1):
    A = list(input())
    B = A[:]
    N = len(A)
    for i in range(N//2):
        if A[i] != A[N-1-i]:
            A.pop(i)
            B.pop(N-1-i)
            if A == list(reversed(A)) or B == list(reversed(B)):
                print(1)
                break
            else:
                print(2)
                break
    else:
        print(0)