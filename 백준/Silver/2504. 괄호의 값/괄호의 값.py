import sys
input = sys.stdin.readline

sho = input().rstrip()

stack = []
for i in range(len(sho)):
    if sho[i] == '(' or sho[i] == '[':
        stack.append(sho[i])
    elif sho[i] == ')':
        if stack:
            if stack[-1] == '(':
                stack.pop()
            else:
                print(0)
                break
        else:
            print(0)
            break
    elif sho[i] == ']':
        if stack:
            if stack[-1] == '[':
                stack.pop()
            else:
                print(0)
                break
        else:
            print(0)
            break
else:
    if stack:
        print(0)
    else:
        sho = sho.replace('()', '2').replace('[]', '3')
        # print(sho)
        A = list(sho)

        while True:
            for i in range(len(A)-2):
                # print(A[i] + A[i + 2])
                if A[i]+A[i+2] in ['()', '[]']:
                    # print(A[i]+A[i+2])
                    if A[i] == '(':
                        A[i:i+3] = [str(2*int(A[i+1]))]
                        # print(A)
                    else:
                        A[i:i + 3] = [str(3 * int(A[i+1]))]
                        # print(A)
                    break
            else:
                temp = []
                for i in range(len(A)):
                    if A[i].isdigit():
                        temp.append(int(A[i]))
                    else:
                        if len(temp) >= 2:
                            A[i-len(temp):i] = [str(sum(temp))]
                            # print(A)
                            break
                        temp = []
                if '(' not in A and '(' not in A and '[' not in A and ']' not in A:
                    ans = 0
                    for k in range(len(A)):
                        ans += int(A[k])
                    print(ans)
                    break

