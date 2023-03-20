# https://school.programmers.co.kr/learn/courses/30/lessons/160585
# X의 수가 더 많거나, X가 이겼을 때 O도 이겼을 경우가 있는지 체크.
# X의 수와 O의 수를 체크
# O가 승리하였는지 체크. -> O이 승리하였을 때 X는 반드시 O보다 하나 적다.
# X가 승리하였는지 체크. -> X가 승리하였을 때 O과 반드시 같은 수이며, O는 승리해서는 안된다.
def isWin(x,board):
        list_board = []
        for i in board :
                list_board += i
        conditionToWin = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        for i in conditionToWin:
                for j in i :
                        if list_board[j] != x :
                                break
                else:
                        return True
        return False
def solution(board):
        countX = 0
        countO = 0
        for i in board:
                for j in i:
                        if j == "X":
                                countX += 1
                        elif j == "O":
                                countO += 1
        if countX > countO :
                return 0
        elif countX == countO :
                if isWin("O",board) :
                        return 0
        else : # countO가 더 많을 경우
                if countO - 1 != countX:
                        return 0
                if isWin("X",board) :
                        return 0
        return 1