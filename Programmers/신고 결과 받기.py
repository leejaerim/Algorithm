# 문제명 : 신고 결과 받기
# 사이트 : https://programmers.co.kr/learn/courses/30/lessons/92334?language=python3 
class Person:
    _to = ''
    _from = ''
    def setdata(self,_to,_from):
        self._to = _to
        self._from = _from
    def __str__(self) -> str:
        return self._to + '->' + self._from + '\n'
class Report:
    data = []
    reported = {}
    reportedCnt = {}
    blocked = []
    def updateData(self,listto, listfrom):
        a = Person()
        a.setdata(listto,listfrom)
        self.data.append(a)
    def setblock(self,int):
        for i in self.data:
            if i._to in self.reported:
                self.reported[i._to]+= i._from
            else:
                self.reported[i._to] = i._from
            self.reported[i._to]+= " "
            if i._from in self.reportedCnt:
                self.reportedCnt[i._from] += 1 
            else:
                self.reportedCnt[i._from] = 1

        self.printReported(int)
    
    def printReported(self, int):
        for i in self.reportedCnt:
            if self.reportedCnt[i] >= int:
                self.blocked.append(i)
        
    def returnMessage(self,list):
        answer = []
        cnt = 0
        for i in list:
            for j in self.blocked:
                if i in self.reported:
                    if j in  self.reported[i].split(' '):
                        cnt +=1
            answer.append(cnt)
            cnt  = 0

        return answer
    def __str__(self) -> str:
        res = ''
        for i in self.data:
            res+=i.__str__()
        return res
def solution(id_list, report, k):
    _list = set(report)
    res = list(_list)
    answer = []
    a = Report()
    for i in res:
        reslist = i.split(' ')
        a.updateData(reslist[0],reslist[1])
        
    a.setblock(k)
    answer = a.returnMessage(id_list)
        

    return answer
print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3))


#######Best Answer

def best_solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

# 레포트의 람다함수와 set을 이용한 중복 제거 , list.index (내장함수) 등 미숙지로 오브젝트를 만드는 등 복잡하게 구현했다.
# 반성할 부분 : 회고 해보면 딕셔너리 item()을 써서 반복문 키,값으로 출력하지도 않았거니와, 반복문 이터레이터의 존재도 모르고 있었다. 
# 좋았던 부분 : 파이썬 애로우함수로 표현해보아서 좋았고, 클래스를 직접 만들어서 self나 메서드 등을 구현해 볼수 있어서 좋았다.