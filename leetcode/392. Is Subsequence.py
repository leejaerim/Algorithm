class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        res_t = list(t)
        res_s = list(s)
        for i in res_s :
            if not i in res_t:
                return False
            else:
                res_t = res_t[res_t.index(i)+1:]
        return True