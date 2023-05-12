from datetime import timedelta
from heapq import heappush
def getMinutes(start:str, end:str)->int:
    sh, sm = start.split(':')
    eh, em = end.split(':')
    time_1 = timedelta(hours= int(sh) , minutes=int(sm))
    time_2 = timedelta(hours= int(eh), minutes=int(em))
    return int((time_2 - time_1).seconds/60)
def solution(m:str, info:list)->str:
    ans = []
    m = m.replace("C#","c").replace("D#","d").replace("F#","f").replace("G#","g").replace("A#","a")
    for i in info:
        start_time , end_time, title, code = i.split(',')
        length = getMinutes(start_time,end_time)
        music = ""
        code = code.replace("C#","c").replace("D#","d").replace("F#","f").replace("G#","g").replace("A#","a")
        for j in range(length): #각 음정.
            music += code[j%len(code)]
        if m in music:
            heappush(ans,(-length, title))
    return "(None)" if not ans else ans[0][1]