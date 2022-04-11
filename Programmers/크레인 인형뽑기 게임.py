# 문제명 : 크레인 인형뽑기 게임
# 사이트 : https://https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3

#입출력 예:

board = [[0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 2, 1, 0, 0], [0, 2, 1, 0, 0], [0, 2, 1, 0, 0]]
moves = [1, 2, 3, 3, 2, 3, 1]	


def solution(board, moves):
    answer = 0
    temp = []
    for i in moves:
        for j in board:
            if not j[i-1] == 0:
                if len(temp) == 0: 
                    temp.append(j[i-1])
                    j[i-1] = 0
                else :
                    if temp[-1] == j[i-1]:
                        temp.pop()
                        answer += 2
                    else:
                        temp.append(j[i-1])
                        j[i-1] = 0
                break
    return answer

print(solution(board,moves))