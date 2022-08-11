class Solution:
    def generateInner(self, n: int , op : int , cl : int , _str:str, res :list)-> None:
        if n ==op and cl == op:
            res.append(_str)    
        if op < n :
            self.generateInner(n,op+1, cl, _str+"(",res)
        if cl < op :
            self.generateInner(n,op,cl+1,_str +")",res)
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.generateInner(n,0,0,"",res)
        return res