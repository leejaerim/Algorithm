class Solution:
    def reverse(self, x: int) -> int:
        isMinus = False
        if x < 0 :
            x = abs(x)
            isMinus = True
        arrstr = str(x)
        if isMinus :
            arrstr = '-'+arrstr[::-1]
        else :
            arrstr = arrstr[::-1]
        x = int(arrstr)
        if x < pow(-2,31) : 
            return 0
        if x >= pow(2,31)-1:
            return 0
        return x
            