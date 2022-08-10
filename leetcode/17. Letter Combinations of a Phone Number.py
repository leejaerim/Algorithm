class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        dict = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        for i in digits:
            res = self.mulmatrix(res, dict[i])
        return res
    def mulmatrix(self, list1:list , list2:list)->List[str]:
        if len(list1) == 0 :
            return list2
        res = []
        for i in list1:
            for j in list2:
                res.append(i+j)
        return res