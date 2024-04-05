A = input().split(":")
# print(A)
if len(A) == 9:
    for i in range(len(A)):
        if A[i] == "":
            A[i:i+2] = ["0000"]
            break
if len(A) <= 8:
    temp = 8 - len(A)
    for i in range(len(A)):
        if A[i] == "":
            A = A[:i] + ['0000'] * (temp + 1) + A[i + 1:]
            break
# print(A)
for i in range(len(A)):
    if len(A[i]) < 4:
        temp = 4 - len(A[i])
        A[i] = '0' * temp + A[i]
result = ":".join(A)
print(result)
