import sys
from itertools import permutations

input = sys.stdin.readline
N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
p2 = list(map(int, input().split()))  # 경희
p3 = list(map(int, input().split()))  # 민호
jiwoo = [i + 1 for i in range(N)]  # 지우


def dfs(cur_p1, cur_p2, idx, win_cnt, players):
    global result

    # 지우가 이긴 경우
    if win_cnt[0] == K:
        result = 1
        return

    # 민호 or 경희가 이긴 경우
    if win_cnt[1] == K or win_cnt[2] == K:
        return

    # 지우가 낼 수 있는 손동작이 없는 경우
    if idx[0] == N:
        return

    next_p = 3 - (cur_p1 + cur_p2)
    move1, move2 = players[cur_p1][idx[cur_p1]] - 1, players[cur_p2][idx[cur_p2]] - 1
    idx[cur_p1] += 1
    idx[cur_p2] += 1

    # 승자 결정
    winner = cur_p1 if (board[move1][move2] == 2 or (board[move1][move2] == 1 and cur_p1 > cur_p2)) else cur_p2

    win_cnt[winner] += 1
    dfs(winner, next_p, idx, win_cnt, players)


result = 0

for p1 in permutations(jiwoo, N):
    players = [p1, p2, p3]  # 지우, 경희, 민호가 낼 전체 손동작 리스트
    idx = [0, 0, 0]  # 각 플레이어의 현재 손동작 인덱스
    win_cnt = [0, 0, 0]  # 각 플레이어의 이긴 횟수

    dfs(0, 1, idx, win_cnt, players)

    if result == 1:
        print(1)
        break
else:
    print(0)