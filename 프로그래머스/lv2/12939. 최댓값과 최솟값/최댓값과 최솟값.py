def solution(s):
    answer0 = list(s.split())
    for i in range(len(answer0)):
        answer0[i] = int(answer0[i])
    answer1 = sorted(answer0)
    answer = str(answer1[0]) + " " + str(answer1[-1])
    return answer