import sys

n, m = map(int, sys.stdin.readline().split())  # 건물 n, 도로 m
INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 자기 자신은 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 1. 모든 정점에서 모든 정점으로 가는  최소 거리 구하기
for k in range(1, n + 1):
    for a in range(1, n + 1):   # 출발 노드
        for b in range(1, n + 1):   # 도착 노드
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 2. 2개의 건물을 선택하여(예상 치킨집) 모든 집을 방문해서 걸리는 거리를 측정 
min_sum = INF
result = list()
for i in range(1, n):  # 건물 2개를 뽑는다.
    for j in range(2, n + 1):
        sum_ = 0
        for k in range(1, n + 1):  # 모든 집을 방문하면서 거리를 측정
            sum_ += min(graph[k][i], graph[k][j]) * 2  # k -> i, k -> j 중에 짧은 거리 합치기
        if sum_ < min_sum:
            min_sum = sum_
            result = [i, j, sum_]

print(*result)