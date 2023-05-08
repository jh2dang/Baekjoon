import sys
input = sys.stdin.readline

n, k, d = map(int, input().split())

algo = [0 for _ in range(k+1)]

student = [[] for _ in range(n)]


for student_num in range(n):
    student_data = list(map(int, input().split()))
    student_data.append(list(map(int, input().split())))

    student[student_num] = student_data.copy()

student.sort(key = lambda x: x[1])


sum_know_algo = 0

sub_know_algo = 0

i = 0
j = 0

answer = -1

while True:
    if student[i][1] - student[j][1] > d:
        for algo_num in student[j][2]:
            algo[algo_num] -= 1
            if algo[algo_num] == 0:
                sum_know_algo -= 1

        j += 1

    if student[i][1] - student[j][1] <= d:
        sub_know_algo = 0
        
        for algo_num in student[i][2]:
            algo[algo_num] += 1
            
            if algo[algo_num] == i - j + 1:
                sub_know_algo += 1
                
            if algo[algo_num] == 1:
                sum_know_algo += 1

        answer = max(answer, (sum_know_algo - sub_know_algo) * (i - j + 1))

        i += 1
        
    if i == n:
        break

print(answer)