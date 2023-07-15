#시간초과
def solution(n, left, right)->list:
    answer = []
    for j in range(n):
        answer += [i+1 if j <= i else j+1 for i in range(n)]
    return answer[left:right+1]

def solution(n, left, right)->list:
    answer = []
    #몇번째부터 시작하는지 검색
    start = left // n
    right = right -(start*n)
    left = left % n
    #right까지 검색했다면
    while len(answer) <= right+1:
        answer += [i+1 if start <= i else start+1 for i in range(n)]
        start+=1
    return answer[left:right+1]