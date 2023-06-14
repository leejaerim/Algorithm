from math import ceil

def calTime(time:str)->int:
    h, m = time.split(":")
    return int(h)*60 + int(m)
def solution(fees:list, records:list)->list:
    answer = []
    #차 넘버를 기준으로 키 밸류, 즉 딕셔너리로 관리합니다.
    car_list = {}
		#차 넘버를 key값으로 type, time 으로 파싱합니다. O(N)
    for i in records :
        time,key,type = i.split(" ")
        if not key in car_list.keys() :
            car_list[key] = [(type,time)]
        else:
            car_list[key].append((type,time))
		#파싱된 딕셔너리의 키값을 기준으로 누적시간을 구합니다.
    for i in car_list.keys():
        isOuted = True
        started = 0
        total = 0
        for j in car_list[i]:
            type, time = j
            if type == 'IN':
                started = calTime(time)
                isOuted = False
            else:
                total += calTime(time) - started
                isOuted = True
                started = 0
        if not isOuted :
            total += calTime("23:59") - started
        answer.append((i,total))
    # 누적시간을 기준으로 요금계산
    cal = []
    for i in answer :
        key, value = i
        fee = 0
        if value <= fees[0] :
            fee = fees[1]
        else:
            fee = fees[1] + ceil((value - fees[0])/fees[2]) * fees[3]
        cal.append((int(key),fee))
    cal.sort(key=lambda x:x[0])
    return list(map(lambda x:x[1],cal))