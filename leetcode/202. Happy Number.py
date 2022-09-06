class Solution:
    def helper(self, n:int , _list : list) -> bool:
        try:
            if n == 1 :
                return True
            else:
                res = 0 
                if n in _list :
                    return False
                _list.append(n)
                for i in str(n):
                    res += int(i)**2
                return self.helper(res, _list)
        except:
            return False
    def isHappy(self, n: int) -> bool:
        return self.helper(n,[])
                