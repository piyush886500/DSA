class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        xorr=nums[0]
        for i in range(1,len(nums)):
            xorr = xorr^nums[i]
        
        return xorr

