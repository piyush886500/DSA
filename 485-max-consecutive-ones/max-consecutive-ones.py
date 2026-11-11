class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_count=0
        count = 0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            elif nums[i]!=1:
                count=0
            if max_count<count:
                max_count = count
        return max_count