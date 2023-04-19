def solution(maps):
    wid = len(maps) - 1
    height = len(maps[0]) - 1
    queue = [(0, 0)]
    while queue:
        i, j = queue.pop(0)
        if i + 1 <= wid and maps[i + 1][j] == 1:
            maps[i + 1][j] = maps[i][j] + 1
            queue.append((i + 1, j))
        if j + 1 <= height and maps[i][j + 1] == 1:
            maps[i][j + 1] = maps[i][j] + 1
            queue.append((i, j + 1))
        if i - 1 >= 0 and maps[i - 1][j] == 1:
            maps[i - 1][j] = maps[i][j] + 1
            queue.append((i - 1, j))
        if j - 1 >= 0 and maps[i][j - 1] == 1:
            maps[i][j - 1] = maps[i][j] + 1
            queue.append((i, j - 1))
    return maps[wid][height] if maps[wid][height] != 1 else -1


# dfs(재귀)가 아닌 bfs(반복)로 풀었다는 점에 생각할 필요가 있다.
# bfs로 접근함으로써, 인접한 경로는 최단 경로로 설정되고 한번 설정된 값이 최소(최단)거리기 때문에 maps[i][j] 가 1 인지만 탐색하면 되기 때문이다.

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])