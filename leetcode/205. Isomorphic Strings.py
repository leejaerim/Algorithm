class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        _dict = {}
        memo = []
        for i,k in enumerate(s):
            try:
                if _dict[k] != t[i]:
                    return False
            except:
                if t[i] in memo :
                    return False
                _dict[k] = t[i]
                memo.append(t[i])            
        return True