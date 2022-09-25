class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if i[0] <= target :
                for j in i : #-> 40.91%
                    if j == target :
                        return True
#                if target in i: -> 33%
#                   return True 
            else:
                return False