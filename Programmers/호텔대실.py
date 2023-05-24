def help(time:str)->str:
    h,m = list(map(lambda x : int(x) ,time.split(":")))
    if m + 10 >= 60:
        m -= 50
        h += 1
    else:
        m += 10
    h = str(h)
    m = str(m)
    if len(h) == 1 : h = "0"+h
    if len(m) == 1 : m = "0"+m
    return h+":"+m
def solution(time:list)->int:
    #정렬할 필요가 있음. -> 마지막 endtime만 비교.
    time = sorted(time, key=lambda x:x[0])
    #결과를 담은 rooms는 어떤 자료구조를 사용할 것인가? dict? list?
    rooms = []
    for i,j in time :
        for index, end_time in enumerate(rooms):
            #add room
            if end_time <= i :
                rooms[index] = help(j)
                break
        else:
            rooms.append(help(j))
    return len(rooms)

#help함수를 둬서, 문자열로 바꿔서 풀었지만,
#그냥 time int type으로 풀어도 무방하다.
# start, end = list(map(lambda x: int(x),"10:05".split(":")))
# time = start*60 + end + 10