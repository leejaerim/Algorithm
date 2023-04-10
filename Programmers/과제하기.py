def solution(_list:list)->list:
    _list.sort(key= lambda x : x[1])
    ans = []
    stack = []

    for name, time, play in _list:
        if len(stack) > 0:
            c_time = None
            while len(stack) > 0:
                t_name, t_time, t_play = stack.pop()
                if c_time is not None:
                    t_time = c_time
                if getTime(t_time, t_play) > time:
                    t_play = t_play - subTime(time,t_time)
                    t_time = time
                    stack.append((t_name , t_time, t_play))
                    break
                else:
                    c_time = getTime(t_time,t_play)
                    ans.append(t_name)
        stack.append((name , time, int(play)))
    while len(stack) > 0:
        t_name, t_time, t_play = stack.pop()
        ans.append(t_name)
    return ans
def subTime(_str1:str, _str2:str)->int:
    h1,m1 = _str1.split(':')
    h2,m2 = _str2.split(':')
    h = int(h1) - int(h2)
    m = int(m1) - int(m2)
    return m + h*60
def getTime(_str:str, _int:int)->str:
    h, m = _str.split(':')
    while int(_int) >= 60:
        _int = int(_int)-60
        h = str(int(h)+1)
    if (int(m) + int(_int)) >= 60:
        h = str(int(h)+1)
        m = str(int(m)+int(_int)-60)
    else:
        m = str(int(m)+int(_int))
    if len(m) == 1:
        m = "0" + m
    if len(h) == 1 :
        h = "0" + h
    return f'{h}:{m}'