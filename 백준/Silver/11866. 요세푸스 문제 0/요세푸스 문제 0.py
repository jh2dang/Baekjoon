from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
queue = deque([int(i) for i in range(1, N+1)])

rlt = []


while queue:
    for _ in range(M-1):
        queue.append(queue.popleft())
    rlt.append(queue.popleft())

print('<',end='')
print(*rlt, sep=', ',end='')
print('>')

