def location(maps:list, queries:list)->list:
    ans = []
    for q in queries:
        x,y,i,j = q
        n = x
        m = y
        prev = maps[x-1][y-1]
        min_val = prev
        while y+1 <= j:
            y += 1
            temp = maps[x-1][y-1]
            maps[x-1][y-1]  = prev
            prev = temp
            if prev <  min_val:
                min_val = prev
        while x+1 <= i:
            x += 1
            temp = maps[x-1][y-1]
            maps[x-1][y-1]  = prev
            prev = temp
            if prev <  min_val:
                min_val = prev
        while y-1 >= m:
            y -= 1
            temp = maps[x-1][y-1]
            maps[x-1][y-1]  = prev
            prev = temp
            if prev <  min_val:
                min_val = prev
        while x-1 >= n:
            x -= 1
            temp = maps[x-1][y-1]
            maps[x-1][y-1] = prev
            prev = temp
            if prev <  min_val:
                min_val = prev
        ans.append(min_val)
    return ans

def solution(rows, columns, queries):
    maps = []
    for i in range(rows):
        maps.append(list(map(lambda x : x, range(i*columns + 1,(i+1)*columns+1))))
    return location(maps,queries)
solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]])