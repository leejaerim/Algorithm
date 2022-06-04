class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        res = []
        col = []
        num = 0
        for i in mat:
            for j in i:
                num += 1
                col.append(j)
                if len(col) == c:
                    res.append(col)
                    col = []
        if num != r*c :
            return mat
        return res