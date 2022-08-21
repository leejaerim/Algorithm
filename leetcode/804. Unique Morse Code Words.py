class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        _dict = {}
        _res = {}
        num = 97
        for i in morse:            
            _dict[chr(num)] = i
            num += 1
        for i in words:
            res = ""
            for j in i:
                res += _dict[j] 
            _res[res] = 1
        return len(_res)