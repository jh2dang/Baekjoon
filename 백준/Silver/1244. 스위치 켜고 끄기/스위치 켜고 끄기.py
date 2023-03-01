import sys
input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))
P = int(input())
for _ in range(P):
    s, n = map(int, input().split())
    if s == 1:
        for i in range(N):
            if (i+1) % n == 0:
                if S[i] == 0:
                    S[i] = 1
                else:
                    S[i] = 0
    else:
        k = 0
        while True:
            if n-1-k >= 0 and n-1+k < N:
                if S[n-1-k] == S[n-1+k]:
                    if S[n-1-k] == 0:
                        S[n-1 - k] = S[n-1 + k] = 1
                    else:
                        S[n-1 - k] = S[n-1 + k] = 0
                    k += 1
                else:
                    break
            else:
                break
while len(S) >= 20:
    print(*S[:20])
    S = S[20:]
print(*S)