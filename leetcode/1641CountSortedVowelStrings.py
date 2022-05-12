class Solution:
    def countVowelStrings(self, n: int) -> int:
        _list = [1,1,1,1,1]
        _temp = [0,0,0,0,0]
        for i in range(0,n):
            _temp[0] = _list[0]+_list[1]+_list[2]+_list[3]+_list[4]
            _temp[1] = _list[1]+_list[2]+_list[3]+_list[4]
            _temp[2] = _list[2]+_list[3]+_list[4]
            _temp[3] = _list[3]+_list[4]
            _temp[4] = _list[4]
            _list = _temp
         return _list[0]