class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(0,n+1):
            res.append(list(format(i, "b")).count('1'))
        return res
# format(i, 'b') -> int to str(binary)