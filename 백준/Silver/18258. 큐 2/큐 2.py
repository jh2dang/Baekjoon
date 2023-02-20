from collections import deque
import sys

input = sys.stdin.readline
queue = deque()

T = int(input())
for _ in range(1, T+1):
    a = input().split()
    order = a[0]

    if order == 'push':
        queue.append(int(a[1]))
    elif order == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif order == 'size':
        print(len(queue))
    elif order == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif order == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif order == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)