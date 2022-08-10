class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        out = set()
        for i in range(0,len(nums)):
            j = i + 1
            k = len(nums)-1
            while(j<k):
                target = nums[i] + nums[j] + nums[k]
                if  target == 0:
                    out.add(tuple([nums[i] , nums[j] , nums[k]]))
                    j += 1
                elif target < 0 :
                    j += 1
                else:
                    k -= 1
        return list(out)

### TIL
# Using SET Object, to avoid duplicate array of number.
# in sorted Circulator, the Pointers (j,k) are useful to compare Number