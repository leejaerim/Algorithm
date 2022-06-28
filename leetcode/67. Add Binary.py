class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = 0
        for i, k in enumerate(a[::-1]):
            res += pow(2,i)*int(k)
        for i, k in enumerate(b[::-1]):
            res += pow(2,i)*int(k)
        return format(res,"b").__str__()

# Best Answer i think
# int(a, 2) + int(b, 2)