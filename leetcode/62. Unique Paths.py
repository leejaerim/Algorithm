 # def helper(self, m : int, n : int, target : list) -> None :
    #     x, y = target
    #     #print(f'x = {x}, y = {y}, m = {m}, n = {n}, \n res = {self.res}')
    #     if m == x - 1 and n == y -1 :
    #         self.res += 1
    #     if m != x - 1 :
    #         self.helper(m+1,n,target)
    #     if n != y -1 :
    #         self.helper(m,n+1, target)
#-> Time out -> dynamic programming
class Solution:
    res = [[0]]
    def helper(self, m : int , n : int) -> None:
        self.res = [[0]]
        try :
            if m == 1 or n == 1:
                return 1
            return self.res[m-1][n-1]
        except:
            for i in range(1,m):
                for j in range(1,n):
                    if i  == 1 :
                        self.res[0].append(1)
                    if j == 1 :
                        self.res.append([1])
                    self.res[i].append(self.res[i-1][j] + self.res[i][j-1])
            return self.res[m-1][n-1]
    def uniquePaths(self, m: int, n: int) -> int:
        if m > n :
            temp = m 
            m = n
            n = temp
        return self.helper(m,n)