def solution(maps):
    target = get_path_target(maps)
    answer = (recur_(maps,target["S"],target["L"]) + recur_(maps,target["L"],target["E"]))
    return -1 if answer >= 9999 else answer

def recur_(maps,start:tuple, end:tuple):
    check = []
    wid = len(maps)
    height = len(maps[0])
    queue = [(start, 0)]
    res = 9999
    x,y = end
    while queue:
        target, nums = queue.pop(0)
        if not target in check :
            check.append(target)
            i, j = target

            if i == x and j == y:
                res = min(res,nums)
                break;
            if i+1 < wid and maps[i+1][j] != "X":
                queue.append(((i+1,j),nums+1))
            if j+1 < height and maps[i][j+1] != "X":
                queue.append(((i,j+1),nums+1))
            if i-1 >= 0 and maps[i-1][j] != "X":
                queue.append(((i-1,j),nums+1))
            if j-1 >= 0 and maps[i][j-1] != "X":
                queue.append(((i,j-1),nums+1))
    return res

def get_path_target(maps):
    target = {}
    for i, v in enumerate(maps):
        for j , w in enumerate(v):
            if w == "S" :
               target["S"] = (i,j)
            if w == "E" :
               target["E"] = (i,j)
            if w == "L" :
               target["L"] = (i,j)
    return target



# 튜플, 튜플 해체(혹은 구조분해), bfs 를 통해서 구현하였습니다.
# 미로 혹은 bfs 알고리즘에 대해 적응할 수 있는 응용력을 공부하였습니다.
