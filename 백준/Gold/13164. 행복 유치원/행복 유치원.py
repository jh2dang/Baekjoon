import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(sorted(list(map(int, input().split()))))
if K == 1: print(A[-1]-A[0])
elif N == K: print(0)
else:
    cha = []
    for i in range(1, len(A)):
        cha.append(A[i]-A[i-1])
    cha = list(reversed(list(sorted(cha))))
    print(sum(cha[K-1:]))