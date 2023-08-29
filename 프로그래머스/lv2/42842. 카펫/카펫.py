def solution(brown, yellow):
    hob = (brown - 4) // 2
    answer = []
    for i in range(hob, 0, -1):
        if yellow % i == 0:
            y = yellow // i
            if i + y == hob:
                answer = [i+2, y+2]
                break
    return answer