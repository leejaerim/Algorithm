#13. Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        Symbol = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        MAX = 10000
        peek = MAX
        res = 0
        for  i in s:
            if peek < Symbol[i]:
                res = res - 2*peek
            res += Symbol[i]
            peek = Symbol[i]
        return res