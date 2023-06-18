from collections import deque
def solution(board:list)->int:
    wid = len(board[0])
    height = len(board)
    arrow = [[1,0],[0,1],[-1,0],[0,-1]] #아래,오른쪽, 위, 왼쪽
    stack = deque([]) #최소값에 도달하기 위해서 DFS가 아닌 popleft 부터 로직 검사 (BFS)
    memorize = set()
    #R의 위치 찾음
    for idx, v in enumerate(board):
        for idy, j in enumerate(v):
            if j == 'R':
                stack.append((idx,idy,0))
                memorize.add((idx,idy))
                break;
    #BFS로 구현하였는데, DFS , BFS 차이점 학습해두기
    while stack:
        x, y, cnt = stack.popleft()
        if board[x][y] == 'G':
            return cnt
        else:
            for xa,ya in arrow :
                temp_x,temp_y = x,y
                #벽이나 장애물에 부딪힐때까지 진행
                while 0 <= temp_x + xa <height and 0<= temp_y + ya < wid and board[temp_x+xa][temp_y+ya] != 'D':
                    temp_x += xa
                    temp_y += ya
                #메모라이즈된 부분인지 체크, 즉 역행 금지
                if not (temp_x,temp_y) in memorize:
                    memorize.add((temp_x,temp_y))
                    stack.append((temp_x,temp_y,cnt+1))
    #stack 다 찾았는데, 없다면 진입 불가 -1 리턴
    return -1