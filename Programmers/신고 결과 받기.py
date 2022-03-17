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

