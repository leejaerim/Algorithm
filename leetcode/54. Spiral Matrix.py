class Solution:
    def helper(self,matrix:List[List[int]])-> List[int]:
        res = []
        res += matrix[0]
        del matrix[0]
        if len(matrix) == 0:
            return res
        col = len(matrix[0])
        row = len(matrix)
        if col == 1:
            while(len(matrix) != 0):
                res.append(matrix[0][0])
                del matrix[0]
            return res
        height = 0
        while(height != row-1):
            res.append(matrix[height][col-1])
            del matrix[height][col-1]
            height+=1
        res+=matrix[height][::-1]
        del matrix[height]
        height -= 1
        while(height > -1):
            res.append(matrix[height][0])
            del matrix[height][0]
            if len(matrix[height]) == 0 :
                del matrix[height]
            height -= 1
        if len(matrix) == 0:
            return res
        res += self.helper(matrix)
        return res
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return self.helper(matrix)
                
                