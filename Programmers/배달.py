#dijkstra algo
def solution(n:int, load:list, k:int)->int:
    UNREACHABLE = 500001
    dik = []
    for i in range(n):
        dik.append([UNREACHABLE]*n)
    for i in range(n):
        dik[i][i] = 0
    for i in load:
        a, b , c = i
        if dik[a-1][b-1] > c:
            dik[a-1][b-1] = c
            dik[b-1][a-1] = c

    for i in range(n):
        for x in range(n):
            for y in range(n):
                if dik[x][y] > dik[x][i] + dik[i][y]:
                    dik[x][y] = dik[x][i] + dik[i][y]
                    dik[y][x] = dik[x][y]
    return len([i for i in dik[0] if i <= k])