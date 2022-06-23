class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i,k in enumerate(nums):
            if k == val : 
                nums[i] = 51
        nums.sort()
        return len(nums)-nums.count(51)     

#Best Answer i think
    #    try:
    #       while 1:
    #         nums.remove(val)
    #         print(nums)
            
            
    #     except:
          
          

    #       return len(nums)