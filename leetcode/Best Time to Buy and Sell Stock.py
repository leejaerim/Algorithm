class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = 0
        for i,k in enumerate(prices):
            if i == 0:
                buy = k
            else :
                if k - buy > 0:
                    if res < k - buy :
                        res = k -buy
                else:
                    if k < buy:
                        buy = k
        return res