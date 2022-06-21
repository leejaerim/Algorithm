class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"{":"}","(":")","[":"]"}
        temp = ""
        while(not s== temp):
            temp=s  
            s = s.replace("[]","").replace("{}","").replace("()","")
            
        leng = len(s)
        if leng == 0 :
            return True
        if leng<2:
            return False
        if brackets.get(s[0]) == s[leng-1]:
            if leng == 2:
                return True
            else :
                return self.isValid(s[1:-1])
        else : 
            return False
            
                
                