# 69. Sqrt(x)
class Solution:
    def mySqrt(self, x: int) -> int:
        #return math.floor(math.sqrt(x))
        #return int(x**(1/2))
        if not x : return 0
        res = 1
        while(1):
            temp = pow(res,2)
            if temp > x:
                res += -1
                break;
            elif temp == x:
                break;
            res+=1
        return res