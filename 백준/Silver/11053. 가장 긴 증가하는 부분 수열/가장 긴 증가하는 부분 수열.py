from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

L = []

for i in range(N):
    if not L or L[-1] < A[i]:
        L.append(A[i])
    else:
        L[bisect_left(L, A[i])] = A[i]

print(len(L))