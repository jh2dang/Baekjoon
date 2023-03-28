import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(sorted((set(A))))
idx = {B[i] : i for i in range(len(B))}
for i in range(len(A)):
    A[i] = idx[A[i]]
print(*A)