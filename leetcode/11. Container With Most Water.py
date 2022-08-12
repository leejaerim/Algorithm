class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        i = 0
        lastIndex = len(height)-1
        while(i < lastIndex):     
            if height[i] < height[lastIndex]:
                tmp = height[i] * (lastIndex - i)
                i += 1
                if res < tmp:
                    res = tmp
            else:
                tmp = height[lastIndex] * (lastIndex - i)
                lastIndex -= 1
                if res < tmp :
                    res = tmp
        return res                
                