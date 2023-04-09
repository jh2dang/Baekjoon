import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    parent[max(a, b)] = min(a, b)

v, m = map(int, input().split())
parent = list(range(v+1))

edges = [[] for _ in range(v+1)]
result = 0

for i in range(v):
    edges[i] = list(map(int, input().split()))

for i in range(m):
    ex, ey = map(int, input().split())
    union(ex, ey)

D = []
for i in range(v-1):
    for j in range(i+1, v):
        d = ((edges[i][0]-edges[j][0])**2 + (edges[i][1]-edges[j][1])**2)**0.5
        D.append([d, i+1, j+1])

D.sort()

for cost, a, b in D:
    if find(a) != find(b):
        union(a, b)
        result += cost

print(f'{result:.2f}')