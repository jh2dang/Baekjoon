from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = [int(i) for i in range(1, N + 1)]
    queue = deque(A)
    pr = list(map(int, input().split()))

    cnt = 0
    while True:
        q = queue.popleft()
        if pr[q - 1] == max(pr):
            pr[q - 1] = 0
            if q == A[M]:
                cnt += 1
                print(f'{cnt}')
                break
            else:
                cnt += 1
        else:
            queue.append(q)

