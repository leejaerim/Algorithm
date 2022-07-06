class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = []
        res = []
        for i in range(rowIndex+1):
            if i == 0:
                res.append([1])
            else:
                for j in range(i+1):
                    if j == 0 or j == i :
                        row.append(1)
                    else:#
                        row.append(res[i-1][j-1]+res[i-1][j])
                res.append(row)
                row = []
        return res[rowIndex]
        