from itertools import permutations
from heapq import heappush
def solution(expression):
    num = ""
    stack = []
    for char in expression:
        if char in ['+','-','*']:
            stack.append(int(num))
            stack.append(char)
            num = ""
        else:
            num += char
    else:
        stack.append(int(num))
    ans = []
    for i in (list(permutations(['+','-','*'],3))):
        temp = stack.copy()
        for j in i :
            while j in temp:
                idx = temp.index(j)
                if j == '+':
                    temp[idx-1] = temp[idx-1] + temp[idx+1]
                elif j == '*':
                    temp[idx-1] = temp[idx-1] * temp[idx+1]
                else:
                    temp[idx-1] = temp[idx-1] - temp[idx+1]
                del temp[idx+1]
                del temp[idx]
        # heappush(ans, (-abs(temp[0]),abs(temp[0])))
        ans.append(abs(temp[0]))
    return max(ans)
solution("100-200*300-500+20")