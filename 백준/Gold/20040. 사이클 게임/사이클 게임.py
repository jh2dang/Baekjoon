import sys
input = sys.stdin.readline


def parents_check(x):
    if parents[x] != x:
        parents[x] = parents_check(parents[x])
    return parents[x]

def union_check(x,y):
    x = parents_check(x)
    y = parents_check(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

N, M = map(int, input().split())
parents = [i for i in range(N)]
for i in range(1, M+1):
    a, b = map(int, input().split())
    if parents_check(a) == parents_check(b):
        print(i)
        break
    union_check(a, b)
else:
    print(0)