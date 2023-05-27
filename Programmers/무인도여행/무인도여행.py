def solution(maps:list)->list:
    width = len(maps[0])
    height = len(maps)
    isLended = list(map(lambda x : list(map(lambda y : 0,range(width))),range(height)))
    answer = []
    def bfs(x,y)->int:
        ans = 0
        stack = [(x,y)]
        while stack :
            x,y = stack.pop()
            if isLended[x][y] != 1 :
                isLended[x][y] = 1
                ans += int(maps[x][y])
                for arrow in [[0,1],[0,-1],[1,0],[-1,0]]:
                    i,j = arrow
                    if x+i < height and y+j < width and x+i >= 0 and y+j >= 0:
                        if maps[x+i][y+j] != "X":
                            stack.append((x+i,y+j))
        return ans
    for i in range(height):
        for j in range(width):
            if not isLended[i][j] and maps[i][j] != "X":
                answer.append(bfs(i,j))
    return [-1] if len(answer)==0 else sorted(answer)
solution(["XXX","XXX","XXX"])