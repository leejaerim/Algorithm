# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        right = n
        left = 1
        while(left <= right):
            mid = (right + left)//2
            if isBadVersion(mid) == False:
                left = mid+1
            elif isBadVersion(mid) == True:
                if isBadVersion(mid-1) == False:
                    return mid
                right = mid -1
                
        return -1